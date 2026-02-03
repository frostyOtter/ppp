# Frontend Task 04: Display Components (Viewer & Feedback)

## Context
You are part of the **Frontend Team**. You are responsible for the "Output" section, visualizing the results and providing feedback.

## Objectives
1.  Build a `ResultViewer` component to render Markdown.
2.  Implement Loading and Error UI states.

## Detailed Instructions
1.  **Dependencies:**
    *   Install `react-markdown` (and optionally `remark-gfm` for tables).
2.  **`ResultViewer` Component:**
    *   Create `src/components/ResultViewer.tsx`.
    *   Accept `content` (string) as a prop.
    *   Render the markdown content safely.
    *   Style the markdown output (headers, lists) using Tailwind typography (`prose` class from `@tailwindcss/typography` is recommended if allowed, otherwise basic styles).
3.  **Feedback UI:**
    *   Create a **Loading Spinner** (CSS or SVG) to show when `isProcessing` is true.
    *   Create an **Error Message** component to display API errors.

## Definition of Done
*   [ ] `ResultViewer` renders markdown text correctly.
*   [ ] Loading state is visually obvious (spinner/overlay).
*   [ ] Error messages are displayed clearly (e.g., red toast or alert box).
