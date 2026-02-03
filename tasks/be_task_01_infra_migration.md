# Backend Task 01: Infrastructure & Code Migration

## Context
You are part of the **Backend Team**. Your responsibility is the initial setup of the backend environment.
This task prepares the ground for other backend engineers to work.

## Objectives
1.  Establish the `backend/` directory structure.
2.  Migrate existing Python code from the root `src/` to `backend/src/`.
3.  Ensure the root directory is clean of Python source files.

## Detailed Instructions
1.  **Create Backend Directory:**
    *   Create a folder named `backend/` in the project root.
2.  **Move Source Code:**
    *   Move the entire `src/` directory (which contains `parsers/` and `main.py`) into `backend/`.
    *   Resulting path should be `backend/src/`.
3.  **Move Configuration Files:**
    *   Move `requirements.txt` to `backend/requirements.txt`.
    *   Move `.python-version` to `backend/.python-version`.
    *   Move `pyproject.toml` to `backend/pyproject.toml`.
    *   Move `uv.lock` (if exists) to `backend/uv.lock`.
4.  **Root Cleanup:**
    *   Verify that no Python files remain in the root directory (except maybe scripts, but `src/` should be gone).
    *   Update `.gitignore` in the root (or create `backend/.gitignore`) to ignore `__pycache__`, `.venv`, `.env`, `*.pyc`.

## Definition of Done
*   [ ] `backend/` directory exists.
*   [ ] `backend/src/` contains the original python code.
*   [ ] `backend/requirements.txt` exists.
*   [ ] Root directory is clean of source code.
