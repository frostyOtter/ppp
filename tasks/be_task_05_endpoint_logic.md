# Backend Task 05: Endpoint Logic Implementation

## Context
You are part of the **Backend Team**. This task ties everything together by implementing the actual API endpoint that the Frontend will call.

## Objectives
1.  Implement `POST /api/v1/parse`.
2.  Handle file uploads and dispatch to the correct parser.
3.  Return a standardized JSON response.

## Detailed Instructions
1.  **Create Endpoint:**
    *   In `backend/src/main.py` (or a dedicated `router.py`), create a POST route `/api/v1/parse`.
2.  **Define Inputs:**
    *   Use `FastAPI`'s `UploadFile` for the PDF file.
    *   Use `Form` or `Query` parameters for:
        *   `parser_type`: str (validate against: docling, pdfminer, pymupdf, pypdf2).
        *   `start_page`: int (optional, default 0).
        *   `max_pages`: int (optional, default 10).
3.  **Implement Logic:**
    *   Save the uploaded file to a temporary location (use `tempfile` module).
    *   Based on `parser_type`, instantiate the correct parser class (import them from `backend.src.parsers...`).
    *   Call the parser's `parse()` method.
    *   Clean up the temp file.
4.  **Return JSON:**
    *   Return a dictionary matching this contract:
        ```json
        {
          "status": "success",
          "metadata": {
            "parser": "docling",
            "pages_processed": 5,
            "filename": "original_filename.pdf"
          },
          "content": "# The Extracted Markdown Content..."
        }
        ```
    *   Handle errors (e.g., file not found, parser error) with `HTTPException` (return 500 or 400).

## Definition of Done
*   [ ] Endpoint `POST /api/v1/parse` exists.
*   [ ] It accepts a PDF file and parser selection.
*   [ ] It successfully calls the refactored parsers.
*   [ ] It returns the correct JSON structure.
