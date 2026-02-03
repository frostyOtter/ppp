# Task 01: Infrastructure & Restructuring

## Context
We are migrating the "PDF Parsers Playground" from a monolithic Streamlit application to a modern Client-Server architecture.
This task focuses on setting up the initial directory structure for the monorepo.

## Objectives
1.  Organize the codebase into a monorepo structure separating `backend` and `frontend`.
2.  Move existing Python code to the `backend` directory.
3.  Initialize the frontend project foundation.

## Detailed Instructions
1.  **Create Directories:**
    *   Create two new directories at the root: `backend/` and `frontend/`.

2.  **Migrate Backend Code:**
    *   Move the existing `src/` directory into `backend/`.
    *   Move `requirements.txt`, `.python-version`, and `pyproject.toml` (if strictly backend related) into `backend/`.
    *   Ensure that `backend/src/parsers/` structure remains intact.

3.  **Initialize Frontend:**
    *   Inside the `frontend/` directory, initialize a new React project using Vite and TypeScript.
    *   Command suggestion: `npm create vite@latest . -- --template react-ts` (or equivalent).
    *   **Do not** implement UI components yet, just the boilerplate.

4.  **Update Configuration:**
    *   Update (or create) a root `.gitignore` to handle both Python (backend) and Node.js (frontend) artifacts (e.g., `__pycache__`, `node_modules`, `dist`, `.venv`).
    *   Ensure `uv.lock` is handled appropriately (moved to backend or root depending on preference, likely backend).

## References
*   `revise_plans/change_plan.md` (Phase 1)
*   `revise_plans/directory_structure.md`

## Definition of Done
*   [ ] Root directory contains `backend/` and `frontend/` folders.
*   [ ] `backend/` contains all original Python source code and dependency files.
*   [ ] `frontend/` contains a valid `package.json` and basic Vite/React structure.
*   [ ] `.gitignore` is updated to exclude artifacts from both sub-projects.
*   [ ] No Python files should remain in the root `src/` (it should be moved or deleted).
