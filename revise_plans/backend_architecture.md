# Backend Architecture Strategy

## Core Decision: FastAPI vs. MCP

The request mentions "maybe change to mcp or just fastapi routers". Here is the analysis for this specific use case.

### 1. FastAPI (Recommended for UI)
Since the primary goal is to build a **Web User Interface** (React/TypeScript), **FastAPI** is the correct choice.
*   **Role:** Acts as the HTTP server that the React frontend calls.
*   **Protocol:** JSON over HTTP.
*   **Why:** Browsers natively speak HTTP. React apps easily consume REST APIs.
*   **Implementation:**
    *   `POST /parse`: Accepts a file upload and configuration parameters.
    *   Returns JSON containing the extracted text (Markdown) and metadata.

### 2. MCP (Model Context Protocol)
MCP is a standard for exposing tools to **LLM Agents** (like Claude or Gemini), not directly to web UIs.
*   **Role:** Allows an AI Assistant to "see" your parsers as tools it can call.
*   **Relevance:** While valuable, it is orthogonal to the goal of "Changing the project to run the UI using TypeScript."
*   **Strategy:** We can implement the parsing logic cleanly so it can be *wrapped* in an MCP server later if desired, but for the React UI, we need a standard REST API first.

## Backend Design (FastAPI)

### Parser Interface Integration
We will treat the existing `parsers/` directory as a library. The API layer will strictly handle HTTP concerns (uploads, validation) and delegate work to the parsers.

#### API Contract (Draft)

**Endpoint:** `POST /api/v1/parse`

**Request (Multipart/Form-Data):**
*   `file`: (Binary) The PDF file.
*   `parser_type`: (String) Enum [`docling`, `pdfminer`, `pymupdf`, `pypdf2`].
*   `start_page`: (Int) Optional, default 0.
*   `max_pages`: (Int) Optional, default 10.

**Response (JSON):**
```json
{
  "status": "success",
  "metadata": {
    "parser_used": "docling",
    "num_pages_processed": 5,
    "processing_time_ms": 1200
  },
  "content": "# Extracted Markdown Content...\n\n..."
}
```

### Refactoring `parsers/`
*   **Current State:** Parsers might be printing logs or tailored for Streamlit.
*   **Required Changes:**
    *   Ensure all parsers inherit from `BaseParser`.
    *   Ensure `parse()` methods return pure strings/objects, not side effects.
    *   Use `loguru` for structured logging instead of `print`.

