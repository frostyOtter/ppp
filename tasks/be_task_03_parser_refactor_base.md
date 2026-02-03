# Backend Task 03: Refactor Base & Docling Parser

## Context
You are part of the **Backend Team**. The existing parsers rely on `streamlit` (e.g., `st.write`). This violates the clean architecture. You need to refactor the Base Parser and the Docling Parser.

## Objectives
1.  Refactor `BaseParser` to define a clean contract.
2.  Refactor `DoclingParser` to return data instead of printing to UI.

## Detailed Instructions
1.  **Refactor `base_parser.py`:**
    *   Locate `backend/src/parsers/base_parser.py`.
    *   Ensure the `parse` method (or equivalent) is abstract or clearly defined to return a `str` (the parsed text) or a `dict`.
    *   **Remove** any `streamlit` imports or calls.
2.  **Refactor `docling_parser.py`:**
    *   Locate `backend/src/parsers/docling_parser.py`.
    *   Remove `import streamlit as st`.
    *   Change the logic so that instead of `st.write(content)`, it **returns** the content.
    *   Use `loguru.logger` for any debug prints.
    *   Ensure it adheres to the `BaseParser` interface.

## Definition of Done
*   [ ] `base_parser.py` has no Streamlit dependencies.
*   [ ] `docling_parser.py` has no Streamlit dependencies.
*   [ ] `docling_parser.py` returns the extracted text/markdown as a string.
