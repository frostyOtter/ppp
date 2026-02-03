# Task 04: Integration & Deployment

## Context
Both Backend and Frontend are implemented. Now we need to ensure they work together seamlessly and provide easy startup instructions.

## Objectives
1.  Orchestrate the services using Docker (optional but recommended) or simple scripts.
2.  Update documentation.
3.  Final verification.

## Detailed Instructions
1.  **Docker Compose (Recommended):**
    *   Create a `Dockerfile` for the `backend/`.
    *   Create a `Dockerfile` for the `frontend/` (multistage build: build -> serve with nginx or just node for dev).
    *   Create a `docker-compose.yml` in the root to spin up both services.
    *   Ensure the frontend container can talk to the backend container (handle CORS if running on different ports locally).

2.  **CORS Configuration:**
    *   Verify that `backend/src/main.py` has `CORSMiddleware` configured to allow requests from the frontend URL (e.g., `http://localhost:5173`).

3.  **Documentation:**
    *   Update the root `README.md`.
    *   Remove Streamlit-specific instructions.
    *   Add "How to Run" section:
        *   **Option A (Docker):** `docker-compose up`
        *   **Option B (Manual):**
            1.  `cd backend && uv run uvicorn ...`
            2.  `cd frontend && npm install && npm run dev`

4.  **Final Verification:**
    *   Perform a full user journey test:
        *   Start apps.
        *   Upload `data/Quizlet Print.pdf` (or similar).
        *   Select `docling` parser.
        *   Verify the output matches expectation.

## References
*   `revise_plans/change_plan.md` (Phase 4)

## Definition of Done
*   [ ] `docker-compose.yml` works (if implemented) or clear shell commands provided.
*   [ ] `README.md` is up-to-date.
*   [ ] Application works end-to-end without CORS errors.
*   [ ] Clean up any leftover temporary files or old Streamlit artifacts.
