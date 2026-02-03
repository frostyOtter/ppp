# Frontend Task 01: Setup & Infrastructure

## Context
You are part of the **Frontend Team**. Your goal is to initialize the project and set up the build tools.
This task prepares the environment for the rest of the frontend team.

## Objectives
1.  Initialize a React + TypeScript project using Vite.
2.  Install and configure TailwindCSS.
3.  Establish the directory structure.

## Detailed Instructions
1.  **Project Initialization:**
    *   In the project root, create the `frontend/` directory (if not exists).
    *   Inside `frontend/`, run: `npm create vite@latest . -- --template react-ts`.
    *   Run `npm install`.
2.  **TailwindCSS Setup:**
    *   Install dependencies: `npm install -D tailwindcss postcss autoprefixer`.
    *   Init config: `npx tailwindcss init -p`.
    *   Configure `tailwind.config.js` to scan `./index.html` and `./src/**/*.{js,ts,jsx,tsx}`.
    *   Add `@tailwind` directives to `src/index.css`.
3.  **Cleanup & Structure:**
    *   Remove default Vite boilerplate (assets, counter example).
    *   Create folders: `src/components`, `src/api`, `src/types`, `src/hooks`.
4.  **Git Ignore:**
    *   Ensure `.gitignore` (in root or frontend) ignores `node_modules`, `dist`, `.env`.

## Definition of Done
*   [ ] `frontend/package.json` exists.
*   [ ] `npm run dev` starts a blank React app with Tailwind working (test with a red text class).
*   [ ] Directory structure (`components`, `api`, etc.) is ready.
