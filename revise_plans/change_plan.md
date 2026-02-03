# Migration Plan: Streamlit to TypeScript + FastAPI

## Overview
This document outlines the steps to migrate the "PDF Parsers Playground" from a monolithic Streamlit application to a modern Client-Server architecture using a TypeScript frontend and a Python FastAPI backend.

## Goals
1.  Decouple the UI from the parsing logic.
2.  Enable a more flexible and interactive UI using TypeScript (React).
3.  Expose the parsing capabilities as a reusable REST API.

## Phases

### Phase 1: Infrastructure & Restructuring
*   **Objective:** Organize the codebase into a monorepo structure separating Backend and Frontend.
*   **Actions:**
    1.  Create `backend/` and `frontend/` directories.
    2.  Move existing Python code (`src/parsers`, `requirements.txt`, etc.) into `backend/`.
    3.  Initialize a new React + TypeScript project in `frontend/`.
    4.  Update `.gitignore` to handle both environments.

### Phase 2: Backend Implementation (Python/FastAPI)
*   **Objective:** Replace `main.py` (Streamlit) with an API server.
*   **Actions:**
    1.  Install `fastapi`, `uvicorn`, and `python-multipart`.
    2.  Create `backend/src/api/` to hold route definitions.
    3.  **Parser Integration:**
        *   Refactor `src/main.py` functionality into API endpoints (e.g., `POST /api/v1/parse`).
        *   Ensure parsers (`docling`, `pdfminer`, etc.) return structured JSON data or clean Markdown instead of directly writing to a Streamlit buffer.
    4.  Implement standardized error handling and logging using `loguru`.

### Phase 3: Frontend Implementation (TypeScript/React)
*   **Objective:** Recreate the UI features in a modern web framework.
*   **Actions:**
    1.  **Tech Stack:** React, Vite, TailwindCSS (for styling), Axios/TanStack Query (for API calls).
    2.  **Components:**
        *   `FileUpload`: specialized component for drag-and-drop.
        *   `ParserSettings`: Form to select the parser (Docling, PyMuPDF, etc.) and configure ranges.
        *   `MarkdownViewer`: Component to render the parsed output (replacing `st.markdown`).
    3.  **State Management:** Handle loading states, error messages, and parsed results.

### Phase 4: Integration & Deployment
*   **Objective:** Run both services together seamlessly.
*   **Actions:**
    1.  Create a `docker-compose.yml` to spin up both the Backend and Frontend services.
    2.  Update `README.md` with new startup instructions.
    3.  Verify full end-to-end flow: Upload PDF -> Backend Process -> Frontend Display.
