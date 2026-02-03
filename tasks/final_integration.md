# Task: Integration & Deployment (Final Phase)

## Context
**Prerequisite:** Both `Backend Development` and `Frontend Development` tasks must be substantially complete.
This task merges the two parallel tracks into a unified, deployable application.

## Objectives
1.  Containerize the application.
2.  Verify end-to-end functionality.
3.  Finalize documentation.

## Detailed Instructions

### 1. Docker Setup
*   **Backend Dockerfile:**
    *   Create `backend/Dockerfile`. Python base image. Install `uv` or `pip`. Expose port 8000. CMD: `uvicorn`.
*   **Frontend Dockerfile:**
    *   Create `frontend/Dockerfile`. Multi-stage build (Node build -> Nginx serve).
*   **Docker Compose:**
    *   Create `docker-compose.yml` in the root.
    *   Define services: `backend` and `frontend`.
    *   Ensure network connectivity between them.

### 2. Final Verification
*   **CORS Check:**
    *   Ensure the Backend's CORS settings allow the Frontend's URL (production or docker internal).
*   **End-to-End Test:**
    *   Spin up the stack: `docker-compose up`.
    *   Open the browser.
    *   Upload `data/Quizlet Print.pdf`.
    *   Verify the parsing happens and results appear.

### 3. Documentation
*   **Clean Up:** Remove any old Streamlit references from `README.md`.
*   **Update README:**
    *   Add clear "How to Run" instructions (Docker vs Manual).
    *   Describe the new architecture (React + FastAPI).

## Definition of Done
*   [ ] `docker-compose up` launches the full application successfully.
*   [ ] The application works seamlessly from a user perspective.
*   [ ] `README.md` is accurate and up-to-date.
*   [ ] Project is ready for release/demo.
