# Frontend Task 05: API Integration & Wiring

## Context
You are part of the **Frontend Team**. Your job is to connect the UI components (Tasks FE-03, FE-04) with the Logic (Task FE-02) and the Backend.

## Objectives
1.  Setup Axios (or Fetch) client.
2.  Implement the "Process" action.
3.  Wire everything together in `App.tsx`.

## Detailed Instructions
1.  **API Client:**
    *   Create `src/api/client.ts`.
    *   Configure Axios base URL to `http://localhost:8000`.
    *   Create a function `uploadPdf(file: File, parser: string, ...)` that sends the `POST /api/v1/parse` request.
2.  **Main Logic (`App.tsx`):**
    *   Import `FileUpload`, `ParserSettings`, `ResultViewer`.
    *   Add a "Process" or "Parse" button.
    *   **On Click:**
        *   Set `isProcessing = true`.
        *   Call `uploadPdf`.
        *   On Success: Update `result` state, set `isProcessing = false`.
        *   On Error: Update `error` state, set `isProcessing = false`.
3.  **Integration:**
    *   Pass state down to components.
    *   Ensure the flow: Upload -> Select -> Click -> Wait -> View Result.

## Definition of Done
*   [ ] Clicking "Process" sends a valid request to the Backend.
*   [ ] The response is successfully displayed in the Viewer.
*   [ ] The application works end-to-end (mocked backend if backend isn't ready, or real if it is).
