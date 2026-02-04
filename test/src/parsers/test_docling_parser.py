import sys
from unittest.mock import MagicMock
import pytest
from src.parsers.docling_parser import DoclingParser

def test_docling_parser_success(mocker):
    # Mock the module that will be imported locally in the function
    mock_docling_module = MagicMock()
    mock_converter_cls = MagicMock()
    mock_docling_module.DocumentConverter = mock_converter_cls
    
    # Mock the conversion result
    mock_result = MagicMock()
    
    # Mock pages and text
    mock_page = MagicMock()
    mock_text_block = MagicMock()
    mock_text_block.text = "Page 1 content"
    mock_page.text_blocks = [mock_text_block]
    mock_result.document.pages = [mock_page]
    
    # Mock metadata
    mock_result.document.metadata = {"Author": "Test Author"}
    
    # Mock tables (empty for now)
    mock_result.document.tables = []
    
    # Mock images (empty for now)
    mock_result.document.images = []
    
    # Set up the converter instance
    mock_converter_instance = mock_converter_cls.return_value
    mock_converter_instance.convert.return_value = mock_result
    
    # Patch sys.modules so that 'import docling.document_converter' returns our mock
    # We need to mock 'docling.document_converter' specifically
    mocker.patch.dict(sys.modules, {"docling.document_converter": mock_docling_module})
    
    parser = DoclingParser()
    result = parser.parse("dummy.pdf", 1, 5)
    
    assert "# Document Analysis" in result
    assert "Test Author" in result
    assert "Page 1 content" in result
    
    # Verify arguments. Note parser uses start_page-1 for 0-based index
    # parse arg: start_page=1, max_pages=5 -> range(0, 5)
    mock_converter_instance.convert.assert_called_once()
    args, kwargs = mock_converter_instance.convert.call_args
    assert args[0] == "dummy.pdf"
    assert kwargs["page_numbers"] == [0, 1, 2, 3, 4]
