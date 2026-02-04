# Frontend Improvement Plan v1: Progressive Multi-Parser Comparison

## 1. Objective
Transform the current single-parser workflow into a compact, progressive, and user-friendly interface that allows comparing results from multiple PDF parsing engines side-by-side.

## 2. User Flow & UX Design
The interface will use a **Progressive Disclosure** pattern. Elements appear only when needed.

1.  **Initial State**:
    -   **Clean Slate**: Only a centered, prominent **Upload Block** is visible.
    -   *Why*: Reduces cognitive load; user focuses on the first task.

2.  **File Review State (After Upload)**:
    -   The Upload Block morphs into a **File Review Card** (Icon, Filename, Size, "Change File" button).
    -   **Parser Selector** appears below the card.
        -   UI: Horizontal or Grid of Checkboxes (Card style).
        -   Default: **None selected** (forces user choice).
    -   **Process Button**: Visible but **Disabled** (Grayed out).

3.  **Ready State**:
    -   User selects one or more parsers (e.g., Docling + PDFMiner).
    -   **Process Button** lights up (Enabled, Blue/Primary Color).

4.  **Processing State**:
    -   User clicks Process.
    -   UI transitions to a **Results Grid**.
    -   Each selected parser gets a card in the grid showing a "Processing..." spinner.

5.  **Results State**:
    -   As requests finish, spinners are replaced by **Result Cards**.
    -   **Result Card Layout**:
        -   **Header**: Parser Name (e.g., "Docling"), Badge (Time taken: 1.2s).
        -   **Body**: Scrollable Markdown Preview.
        -   **Footer**: "Copy", "Expand" actions.

## 3. Technical Architecture (React + Vite)

### 3.1. Server Components vs. Client Components
*Note on User Preference*: The project currently uses **Vite** (Client-Side Rendering). True "React Server Components" (RSC) require a framework like Next.js.
*Strategy*: We will stick to the current **Vite** architecture to avoid a costly migration but use a **Container/Presentational pattern** to keep logic clean and ready for potential future migration.

### 3.2. State Management (`AppContext`)
We need to refactor `AppContext` to handle multiple parsers.

*   **Current**: `parser: ParserType`, `result: ParsedResult | null`
*   **New**:
    ```typescript
    interface AppState {
      file: File | null;
      selectedParsers: Set<ParserType>; // Multi-selection
      results: Map<ParserType, AsyncResult<ParsedResult>>; // Track status per parser
      globalStatus: 'IDLE' | 'REVIEW' | 'PROCESSING' | 'COMPLETED';
    }
    
    type AsyncResult<T> = 
      | { status: 'pending' }
      | { status: 'success', data: T, durationMs: number }
      | { status: 'error', error: string };
    ```

### 3.3. API Integration
The current `uploadPdf` function handles one parser.
*   **Strategy**: The frontend will trigger **parallel requests**, one for each selected parser.
*   *Why*: Better UX (results pop in as they finish) and fault tolerance (one failure doesn't stop others).

## 4. Component Refactoring Plan

### 4.1. `App.tsx` (Layout)
*   Remove the permanent Sidebar. Move configuration into the main flow.
*   Implement a centered, max-width layout container.

### 4.2. `FileReview.tsx` (New Component)
*   Displays the uploaded file details.
*   Includes a "Remove/Change" button to revert to the Upload state.

### 4.3. `ParserSelector.tsx` (Modified `ParserSettings`)
*   Change `<select>` to a list of Checkbox Cards.
*   Props: `selected: Set<ParserType>`, `onToggle: (p: ParserType) => void`.

### 4.4. `ResultGrid.tsx` (New Component)
*   Layout: CSS Grid (`grid-cols-1 md:grid-cols-2 lg:grid-cols-3`).
*   Children: `ResultCard` components.

### 4.5. `ResultCard.tsx` (New Component)
*   Displays content for a single parser.
*   Handles "Loading", "Error", and "Success" states internally based on props.

## 5. Implementation Steps
1.  **Refactor Types & Context**: Update `AppContext` for multi-selection and results map.
2.  **API Client**: Ensure client supports concurrent calls (likely already does, just need to call it multiple times).
3.  **UI - Phase 1 (Input)**: Implement the Progressive Upload -> Review -> Select flow.
4.  **UI - Phase 2 (Output)**: Implement the Grid Layout for results.
5.  **Styling**: Apply Tailwind classes for the "Compact" and "Modern" look.

## 6. Comparison of Approaches

| Feature | Current | Proposed |
| :--- | :--- | :--- |
| **Selection** | Single Dropdown (Sidebar) | Multi-select Checkboxes (Main Flow) |
| **Flow** | Static Layout | Progressive (Upload -> Config -> Result) |
| **Results** | Single View | Grid View (Comparison) |
| **UX** | Functional | Exploratory & visual |

