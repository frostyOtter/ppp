# Task: Backend Development (Parallel Track)

## Context
You are the **Backend Developer**. Your goal is to establish the backend infrastructure and implement the FastAPI server.
This task runs **in parallel** with the Frontend Development. You have full ownership of the `backend/` directory.

## Objectives
1.  Set up the `backend/` directory and migrate existing Python code.
2.  Implement a FastAPI server to expose parsing capabilities.
3.  Refactor existing parsers to be pure functional components (remove Streamlit).

## Detailed Instructions

### 1. Infrastructure Setup
*   **Create Directory:** Create `backend/` at the project root.
*   **Migrate Code:**
    *   Move the existing `src/` directory (containing parsers) into `backend/`.
    *   Move `requirements.txt`, `.python-version`, and `pyproject.toml` into `backend/`.
    *   **Cleanup:** Ensure no Python source files remain in the root `src/` (delete root `src/` if empty).
*   **Git Ignore:**
    *   Update (or create) the root `.gitignore` to exclude Python artifacts (`__pycache__`, `.venv`, `.env`, etc.).

### 2. Dependency Management
*   Navigate to `backend/`.
*   Add the following dependencies to `requirements.txt` (or install via `uv`/`pip`):
    *   `fastapi`
    *   `uvicorn`
    *   `python-multipart`
    *   `loguru` (if not present)

### 3. API Implementation
*   **Structure:** Create `backend/src/api/` and `backend/src/main.py`.
*   **FastAPI App (`src/main.py`):**
    *   Initialize `app = FastAPI()`.
    *   **CORS:** Configure `CORSMiddleware` to allow requests from `http://localhost:5173` (Frontend default).
*   **Endpoint:** Implement `POST /api/v1/parse`.
    *   **Input:** `file` (UploadFile), `parser_type` (Enum: docling, pdfminer, pymupdf, pypdf2).
    *   **Logic:**
        1.  Receive file.
        2.  Instantiate the selected parser from `backend/src/parsers/`.
        3.  Call the parsing method.
        4.  Return JSON response.

### 4. Refactor Parsers
*   Modify files in `backend/src/parsers/`.
*   **Remove Streamlit:** Delete all `st.write`, `st.sidebar`, `st.file_uploader` calls.
*   **Logging:** Replace `print()` with `loguru.logger`.
*   **Return Values:** Ensure methods return structured data (text/JSON), not `None`.

### 5. API Contract (JSON Response)
Ensure your API returns this structure so the Frontend team can consume it:
```json
{
  "status": "success",
  "metadata": { "parser": "docling", "pages": 5 },
  "content": "# Extracted Markdown Content..."
}
```

## Definition of Done
*   [ ] `backend/` directory is fully set up with migrated code.
*   [ ] `uvicorn src.main:app --reload` runs successfully from `backend/`.
*   [ ] `POST /api/v1/parse` works via Curl or Postman.
*   [ ] No Streamlit code remains in parsers.
