# Task 02: Backend Implementation (Python/FastAPI)

## Context
After setting up the infrastructure (Task 01), we need to replace the Streamlit entry point with a FastAPI server. This task involves creating the API layer and adapting the parsers.

## Objectives
1.  Implement a FastAPI backend to expose parsing capabilities.
2.  Refactor parsers to be pure functional components (removing Streamlit specific code).

## Detailed Instructions
1.  **Install Dependencies:**
    *   In `backend/`, add `fastapi`, `uvicorn`, and `python-multipart` to `requirements.txt` (or install via `uv`/`pip`).

2.  **Create API Structure:**
    *   Create `backend/src/api/` directory.
    *   Create `backend/src/main.py` (or update the moved one) to initialize the `FastAPI` app.

3.  **Implement API Endpoint:**
    *   Create an endpoint `POST /api/v1/parse`.
    *   **Inputs:**
        *   `file`: UploadFile (Multipart)
        *   `parser_type`: String (Enum: docling, pdfminer, pymupdf, pypdf2) - *Validate this!*
        *   `start_page`: int (optional)
        *   `max_pages`: int (optional)
    *   **Logic:**
        *   Receive the file.
        *   Instantiate the selected parser from `backend/src/parsers/`.
        *   Call the parsing method.
        *   Return the results as JSON.

4.  **Refactor Parsers:**
    *   Review files in `backend/src/parsers/`.
    *   Ensure they inherit from `BaseParser`.
    *   **Crucial:** Remove any `st.write`, `st.sidebar`, or Streamlit-specific calls. The parsers must return data (strings, dicts), not print to a UI.
    *   Replace `print()` statements with `loguru.logger`.

5.  **Output Format:**
    *   The API should return a JSON response following this structure (draft):
        ```json
        {
          "status": "success",
          "metadata": { "parser": "...", "pages": 5 },
          "content": "# Markdown Content..."
        }
        ```

## References
*   `revise_plans/change_plan.md` (Phase 2)
*   `revise_plans/backend_architecture.md`

## Definition of Done
*   [ ] FastAPI app runs successfully (`uvicorn src.main:app --reload`).
*   [ ] `POST /api/v1/parse` accepts a PDF and returns JSON with extracted text.
*   [ ] All parsers in `src/parsers` are free of Streamlit dependencies.
*   [ ] Structured logging is implemented using `loguru`.
