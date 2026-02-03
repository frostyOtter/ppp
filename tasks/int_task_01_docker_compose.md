# Integration Task 01: Docker & Final Deployment

## Context
**Prerequisite:** All Backend and Frontend tasks are substantially complete.
This task creates the artifacts for running the application easily.

## Objectives
1.  Create Dockerfiles for Backend and Frontend.
2.  Create `docker-compose.yml`.
3.  Update Documentation.

## Detailed Instructions
1.  **Backend Dockerfile (`backend/Dockerfile`):**
    *   Use `python:3.10-slim` (or similar).
    *   Install system deps if needed.
    *   Copy `requirements.txt` and install.
    *   Copy `src/`.
    *   CMD: `uvicorn src.main:app --host 0.0.0.0 --port 8000`.
2.  **Frontend Dockerfile (`frontend/Dockerfile`):**
    *   Stage 1 (Build): Node image, `npm install`, `npm run build`.
    *   Stage 2 (Serve): Nginx image, copy `dist/` to html folder.
3.  **Docker Compose (`docker-compose.yml`):**
    *   Service `backend`: build `./backend`, ports `8000:8000`.
    *   Service `frontend`: build `./frontend`, ports `5173:80` (or whatever nginx port).
4.  **Documentation (`README.md`):**
    *   Clear instructions on how to start the app using Docker.
    *   Clear instructions for manual startup (Dev mode).

## Definition of Done
*   [ ] `docker-compose up --build` works successfully.
*   [ ] App is accessible and functional.
*   [ ] README is updated.
