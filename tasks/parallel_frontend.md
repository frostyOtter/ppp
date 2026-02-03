# Task: Frontend Development (Parallel Track)

## Context
You are the **Frontend Developer**. Your goal is to establish the frontend infrastructure and implement the React UI.
This task runs **in parallel** with the Backend Development. You have full ownership of the `frontend/` directory.

## Objectives
1.  Initialize the React project structure.
2.  Build the UI for file upload and result viewing.
3.  Integrate with the Backend API (assuming the agreed contract).

## Detailed Instructions

### 1. Infrastructure Setup
*   **Create Directory:** Create `frontend/` at the project root.
*   **Initialize Project:**
    *   Run `npm create vite@latest . -- --template react-ts` inside `frontend/`.
*   **Git Ignore:**
    *   Update the root `.gitignore` (or `frontend/.gitignore`) to exclude Node.js artifacts (`node_modules`, `dist`, `.env.local`).

### 2. Environment & Dependencies
*   Install core libraries:
    *   `axios` (or `@tanstack/react-query` + `axios`) for API interaction.
    *   `tailwindcss`, `postcss`, `autoprefixer` for styling.
    *   `react-markdown` to render the parsed output.

### 3. Component Development
*   **`FileUpload`:**
    *   A drag-and-drop zone or file picker.
    *   Must accept `.pdf` files.
*   **`ParserSettings`:**
    *   Dropdown to select parser type (Options: `docling`, `pdfminer`, `pymupdf`, `pypdf2`).
    *   (Optional) Inputs for `start_page` and `max_pages`.
*   **`ResultViewer`:**
    *   A container to display the Markdown response.

### 4. Integration Logic
*   **API Client:**
    *   Configure Axios to point to `http://localhost:8000`.
*   **Process Flow:**
    1.  User selects file & parser.
    2.  Frontend sends `POST` request to `/api/v1/parse` (multipart/form-data).
    3.  **Loading State:** Show a spinner while waiting.
    4.  **Success:** Render `response.data.content` in `ResultViewer`.
    5.  **Error:** Show a toast or error message if the backend fails.

### 5. Expected API Contract
Develop against this expected JSON response:
```json
{
  "status": "success",
  "metadata": { "parser": "...", "pages": 0 },
  "content": "# Markdown Content..."
}
```

## Definition of Done
*   [ ] `frontend/` is initialized and `npm run dev` starts the server (default port 5173).
*   [ ] User Interface allows File Upload and Parser Selection.
*   [ ] "Process" button triggers the API call.
*   [ ] Markdown results are rendered correctly.
*   [ ] Loading and Error states are handled visually.
