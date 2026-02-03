# Backend Task 02: Core API & Dependency Setup

## Context
You are part of the **Backend Team**. Once the infrastructure is ready (Task BE-01), you need to set up the FastAPI application shell and dependencies.

## Objectives
1.  Install necessary backend dependencies.
2.  Initialize the FastAPI app in `backend/src/main.py`.
3.  Configure CORS and Logging.

## Detailed Instructions
1.  **Update Dependencies:**
    *   In `backend/requirements.txt`, add:
        *   `fastapi`
        *   `uvicorn`
        *   `python-multipart`
        *   `loguru`
    *   Install them using your package manager (pip or uv).
2.  **Initialize FastAPI:**
    *   Open (or create) `backend/src/main.py`.
    *   Import `FastAPI` and `CORSMiddleware`.
    *   Initialize the app: `app = FastAPI(title="PDF Parser API")`.
    *   **Delete** any existing Streamlit code in `main.py` (e.g., `st.title`, `st.file_uploader`).
3.  **Configure CORS:**
    *   Add `CORSMiddleware` to `app`.
    *   Allow origins: `["http://localhost:5173"]` (and `*` for dev if preferred).
    *   Allow methods: `["*"]`.
    *   Allow headers: `["*"]`.
4.  **Setup Logging:**
    *   Configure `loguru` to log to console and optionally a file `logs/app.log`.

## Definition of Done
*   [ ] Dependencies installed.
*   [ ] `backend/src/main.py` contains a valid FastAPI app instance.
*   [ ] CORS is enabled for the frontend port.
*   [ ] No Streamlit imports remain in `main.py`.
*   [ ] `uvicorn src.main:app --reload` starts without errors.
