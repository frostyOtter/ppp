# Backend Testing Strategy

This document outlines the testing strategy for the PDF Parser backend. The goal is to ensure the reliability of the API endpoints and the robustness of the various PDF parsing implementations.

## Prerequisites

The following testing libraries are recommended and should be added to `backend/requirements.txt` (or a `requirements-dev.txt`):

*   **`pytest`**: The core testing framework.
*   **`pytest-asyncio`**: For testing asynchronous FastAPI endpoints.
*   **`pytest-mock`**: For mocking external libraries (Docling, PDFMiner, PyMuPDF, etc.) and file system operations.
*   **`httpx`**: For making requests to the FastAPI app during tests.

## Directory Structure

We recommend mirroring the source directory structure for tests:

```text
test/
├── README.md
├── conftest.py          # Shared fixtures (API client, sample PDF paths)
└── src/
    ├── test_main.py     # Tests for FastAPI endpoints in main.py
    └── parsers/
        ├── test_utils.py
        ├── test_docling_parser.py
        ├── test_pdfminer_parser.py
        ├── test_pymupdf_parser.py
        └── test_pypdf2_parser.py
```

## Modules to Test

### 1. API Endpoints (`src/main.py`)

**Why:** To ensure the HTTP interface works as expected, handles file uploads correctly, and routes requests to the correct parser.

**Test Cases:**
*   **`GET /` & `GET /health`**: Verify basic connectivity.
*   **`POST /api/v1/parse` (Success)**: Mock `get_parser` to return a mock parser. Verify that the endpoint calls the parser with correct arguments (file path, page numbers) and returns a 200 OK with the expected JSON structure.
*   **`POST /api/v1/parse` (Invalid Parser)**: Send a request with a `parser_type` not in the allowed list (e.g., "invalid_parser"). Verify a 400 Bad Request response.
*   **`POST /api/v1/parse` (File Upload Error)**: Simulate a file write error or invalid file upload. Verify a 500 Internal Server Error.
*   **`POST /api/v1/parse` (Parser Error)**: Mock the parser to raise an exception. Verify the API handles it gracefully (returns 500 or error detail).

### 2. PDF Parsers (`src/parsers/*.py`)

**Why:** These are the core logic units. They rely heavily on external libraries (Docling, PyMuPDF, etc.) which might not be installed in all environments or might fail on specific files. We need to ensure our wrappers handle these situations correctly.

**General Strategy:** Use `unittest.mock` or `pytest-mock` to mock the underlying libraries (`docling`, `fitz`, `pdfminer`, `PyPDF2`). *Do not* rely on the actual libraries being installed for unit tests.

**Specific Modules:**

*   **`DoclingParser` (`src/parsers/docling_parser.py`)**
    *   **Library Not Installed:** Mock `import docling` to raise `ImportError`. Verify `parse` returns the specific error string.
    *   **Success:** Mock `DocumentConverter` and its `convert` method. Verify `parse` returns markdown with text and tables.
    *   **Conversion Error:** Mock `convert` to raise an exception. Verify error handling.

*   **`PDFMinerParser` (`src/parsers/pdfminer_parser.py`)**
    *   **Library Not Installed:** Mock imports.
    *   **Page Count:** Mock `PDFPage.get_pages`. Test start_page > total_pages logic.
    *   **Text Extraction:** Mock `extract_text` or the complex `PDFResourceManager`/`PDFPageInterpreter` flow. Verify text accumulation.

*   **`PyMuPDFParser` (`src/parsers/pymupdf_parser.py`)**
    *   **File Checks:** Test empty file (0 bytes), invalid header.
    *   **Success:** Mock `fitz.open`. Verify it iterates over pages and calls `get_text`.
    *   **Error Handling:** Mock `fitz.open` to raise exception.

*   **`PyPDF2Parser` (`src/parsers/pypdf2_parser.py`)**
    *   **Encrypted/Corrupt:** Mock `PdfReader` to raise `PdfReadError`.
    *   **Success:** Mock `PdfReader` and `page.extract_text()`.

### 3. Utility Functions (`src/parsers/utils.py`)

**Why:** These helpers provide diagnostic info. If they fail, they shouldn't crash the application, but they should provide useful info.

**Test Cases:**
*   **`pdf_diagnostic_info`**:
    *   Mock `platform`, `sys`, and library imports. Verify the output string contains expected info (OS, Python version).
    *   Test with a non-existent file path.
*   **`analyze_pdf_structure`**:
    *   Mock `fitz` and `PyPDF2` separately to test fallback logic (e.g., if `fitz` fails, does it still try `PyPDF2`?).
