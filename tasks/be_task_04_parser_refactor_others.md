# Backend Task 04: Refactor Legacy Parsers

## Context
You are part of the **Backend Team**. Following the pattern set in Task BE-03, you need to refactor the remaining parsers (`pdfminer`, `pymupdf`, `pypdf2`).

## Objectives
1.  Refactor `PDFMinerParser`, `PyMuPDFParser`, and `PyPDF2Parser`.
2.  Ensure they return data instead of printing to UI.

## Detailed Instructions
1.  **Refactor Loop:**
    *   For each file: `pdfminer_parser.py`, `pymupdf_parser.py`, `pypdf2_parser.py` in `backend/src/parsers/`:
        *   **Remove** `import streamlit as st`.
        *   **Remove** `st.sidebar`, `st.write`, `st.markdown`, `st.spinner`.
        *   Update the `parse()` method to accept the file path (or bytes) and **return** the extracted text.
        *   Replace `print()` with `logger.info()` or `logger.debug()`.
2.  **Standardization:**
    *   Ensure all parsers accept similar arguments (e.g., file path, start page, max pages) as defined in `BaseParser`.

## Definition of Done
*   [ ] All parser files in `backend/src/parsers/` are free of Streamlit code.
*   [ ] All parsers return string/structured data.
*   [ ] Code is clean and uses `loguru` for logging.
