# 🐍 PPP Backend

The backend for the PDF Parser Project, built with **FastAPI** and **Python 3.12**. It serves as the core processing hub, orchestrating different PDF parsing strategies through a clean, hexagonal architecture.

## 🛠 Tech Stack

-   **Language:** Python 3.12+
-   **Framework:** FastAPI
-   **Package Manager:** `uv` (Astral)
-   **Testing:** `pytest`
-   **Parsers:**
    -   `docling`
    -   `pdfminer.six`
    -   `pymupdf` (fitz)
    -   `pypdf2`

## 🚀 Getting Started

### Prerequisites

-   Python 3.12+ installed.
-   `uv` installed (`pip install uv` or via brew/curl).

### Installation

1.  Navigate to the backend directory:
    ```bash
    cd backend
    ```

2.  Sync dependencies:
    ```bash
    uv sync
    ```

### Running the Server

Start the development server with hot-reload:

```bash
uv run fastapi dev src/main.py
```

The API will be available at [http://localhost:8000](http://localhost:8000).
Interactive documentation is at [http://localhost:8000/docs](http://localhost:8000/docs).

## 🧪 Testing

We use `pytest` for unit and integration testing.

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v
```

## 📂 Architecture

The backend code is organized to separate concerns:

```text
src/
├── main.py              # Application entry point
├── parsers/             # Infrastructure Adapters (The Parsers)
│   ├── base_parser.py   # Port interface
│   ├── docling_parser.py
│   ├── pdfminer_parser.py
│   └── ...
└── utils.py             # Shared utilities
```
