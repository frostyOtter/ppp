# Task 03: Frontend Implementation (TypeScript/React)

## Context
With the Backend API ready (Task 02), we need to build the modern UI to replace the Streamlit interface.

## Objectives
1.  Develop a React application to interact with the FastAPI backend.
2.  Replicate the functionality of the original Streamlit app (File Upload -> Select Parser -> View Results).

## Detailed Instructions
1.  **Setup Environment:**
    *   In `frontend/`, install necessary dependencies:
        *   `axios` or `@tanstack/react-query` (for API calls).
        *   `tailwindcss`, `postcss`, `autoprefixer` (for styling).
        *   `react-markdown` (to render the markdown output).

2.  **Develop Components:**
    *   **`FileUpload`**: A component to handle file selection (drag & drop is a plus).
    *   **`ParserSettings`**: A form to select the parser type (Dropdown) and page ranges (Inputs).
    *   **`ResultViewer`**: A component to display the returned Markdown content.

3.  **State Management:**
    *   Manage the state for:
        *   Selected file.
        *   Selected parser options.
        *   Loading/Processing status (show a spinner!).
        *   Error messages.
        *   Parsed result data.

4.  **Integration:**
    *   Connect the components to the `POST /api/v1/parse` endpoint running on the backend.
    *   Handle the API response and display the `content` in the `ResultViewer`.

## References
*   `revise_plans/change_plan.md` (Phase 3)
*   `revise_plans/directory_structure.md`

## Definition of Done
*   [ ] Frontend can be started with `npm run dev`.
*   [ ] User can upload a PDF file.
*   [ ] User can select a parser type.
*   [ ] Clicking "Process" sends the request to the backend.
*   [ ] Resulting Markdown text is rendered nicely on the screen.
*   [ ] Error states (e.g., backend down, invalid file) are handled gracefully.
