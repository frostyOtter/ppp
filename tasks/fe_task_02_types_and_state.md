# Frontend Task 02: Types & State Management

## Context
You are part of the **Frontend Team**. Before building components, we need to define the data structures and how we manage application state.

## Objectives
1.  Define TypeScript interfaces for API responses and application data.
2.  Set up a simple State Management solution (Context API or Zustand - keep it simple).

## Detailed Instructions
1.  **Define Types (`src/types/index.ts`):**
    *   `ParserType`: Enum/Union (`'docling' | 'pdfminer' | 'pymupdf' | 'pypdf2'`).
    *   `ParseResponse`: Interface matching the Backend API:
        ```typescript
        interface ParseResponse {
          status: string;
          metadata: { parser: string; pages_processed: number; filename: string };
          content: string;
        }
        ```
    *   `AppState`: Interface for the app's state (isLoading, error, result, selectedParser, etc.).
2.  **State Management:**
    *   Create a Context (e.g., `AppContext`) or use a simple hook approach.
    *   We need to track:
        *   `file`: File | null
        *   `parser`: ParserType
        *   `isProcessing`: boolean
        *   `result`: ParseResponse | null
        *   `error`: string | null

## Definition of Done
*   [ ] `src/types/index.ts` contains all necessary interfaces.
*   [ ] A way to share state (Context or Hook) is implemented and documented.
