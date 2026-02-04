from unittest.mock import MagicMock
from src.parsers.base_parser import PDFParser
import pytest

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to PDF Parser API"}

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_parse_endpoint_success(client, mocker, sample_pdf_content):
    # Mock the parser instance
    mock_parser_instance = MagicMock(spec=PDFParser)
    expected_content = "# Parsed Content\n\nSome text."
    mock_parser_instance.parse.return_value = expected_content
    
    # Mock get_parser to return our mock instance
    # Note: 'src.main.get_parser' or 'main.get_parser' depends on how it's imported in the test vs app
    # Since we import 'main' in conftest, and test_main uses client which imports main
    # We should patch where it is USED.
    mocker.patch("src.main.get_parser", return_value=mock_parser_instance)

    files = {"file": ("test.pdf", sample_pdf_content, "application/pdf")}
    data = {"parser_type": "docling", "start_page": 0, "max_pages": 5}

    response = client.post("/api/v1/parse", files=files, data=data)

    assert response.status_code == 200
    json_response = response.json()
    assert json_response["status"] == "success"
    assert json_response["content"] == expected_content
    assert json_response["metadata"]["parser"] == "docling"
    assert "duration_ms" in json_response["metadata"]
    assert isinstance(json_response["metadata"]["duration_ms"], float)
    
    # Verify parser was called correctly (start_page + 1)
    mock_parser_instance.parse.assert_called_once()
    # args: (filepath, start_page, max_pages)
    call_args = mock_parser_instance.parse.call_args
    assert call_args[0][1] == 1 # 0 + 1
    assert call_args[0][2] == 5

def test_parse_endpoint_invalid_parser(client, sample_pdf_content):
    files = {"file": ("test.pdf", sample_pdf_content, "application/pdf")}
    data = {"parser_type": "invalid_parser_type"}

    response = client.post("/api/v1/parse", files=files, data=data)

    assert response.status_code == 400
    assert "Invalid parser type" in response.json()["detail"]

def test_parse_endpoint_parser_failure(client, mocker, sample_pdf_content):
    mock_parser_instance = MagicMock(spec=PDFParser)
    mock_parser_instance.parse.side_effect = Exception("Parsing crashed")
    mocker.patch("src.main.get_parser", return_value=mock_parser_instance)

    files = {"file": ("test.pdf", sample_pdf_content, "application/pdf")}
    data = {"parser_type": "docling"}

    response = client.post("/api/v1/parse", files=files, data=data)

    assert response.status_code == 500
    assert "Parsing failed" in response.json()["detail"]

def test_parse_endpoint_too_many_pages(client, mocker, sample_pdf_content):
    # Mock PdfReader to return > 25 pages
    mock_pdf_reader = MagicMock()
    # Create a list of dummy pages > 25
    mock_pdf_reader.pages = [MagicMock()] * 26
    
    # Patch PdfReader in src.main
    mocker.patch("src.main.PdfReader", return_value=mock_pdf_reader)

    # Mock get_parser
    mock_parser_instance = MagicMock(spec=PDFParser)
    mocker.patch("src.main.get_parser", return_value=mock_parser_instance)

    files = {"file": ("large.pdf", sample_pdf_content, "application/pdf")}
    data = {"parser_type": "docling"}

    response = client.post("/api/v1/parse", files=files, data=data)

    assert response.status_code == 400
    assert "Maximum 25 pages allowed" in response.json()["detail"]
    assert "file has 26 pages" in response.json()["detail"]