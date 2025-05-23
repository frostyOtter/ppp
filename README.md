# PDF Parsers Playground (PPP)

A Streamlit application that allows you to experiment with various PDF parsing libraries. This playground provides a user-friendly interface to test and compare different PDF parsing methods, with real-time preview and detailed analysis capabilities.

## Features

- **Interactive PDF Processing**:
  - Upload your own PDF documents
  - Select from pre-populated example PDFs
  - Real-time PDF preview
  - Configurable page range processing
  - Debug visualization support

- **Multiple Parser Support**:
  - PyMuPDF: Fast and reliable text extraction with formatting preservation
  - PyPDF2: Pure-Python PDF processing with basic text extraction
  - PDFMiner: Detailed text extraction with layout analysis
  - Docling: Advanced document understanding with table extraction

- **Comprehensive Analysis**:
  - Markdown-formatted output
  - Raw text extraction
  - Debug visualization
  - PDF structure analysis
  - File diagnostics
  - Metadata extraction

## System Architecture

The application follows a modular architecture with clear separation of concerns:

1. **User Interface Layer**:
   - Streamlit-based web interface
   - File upload and example selection
   - Parser configuration
   - Results visualization

2. **Processing Layer**:
   - PDF validation and preprocessing
   - Parser factory pattern
   - Multiple parser implementations
   - Error handling and logging

3. **Analysis Layer**:
   - Text extraction
   - Table extraction
   - Image detection
   - Structure analysis
   - File diagnostics

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/pdf-parsers-playground.git
cd pdf-parsers-playground
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:
```bash
streamlit run src/main.py
```

## Project Structure

```
pdf-parsers-playground/
├── src/
│   ├── main.py              # Main Streamlit application
│   └── parsers/             # Parser implementations
│       ├── __init__.py      # Parser registry and utilities
│       ├── base_parser.py   # Abstract base class for parsers
│       ├── pymupdf_parser.py
│       ├── pypdf2_parser.py
│       ├── pdfminer_parser.py
│       ├── docling_parser.py
│       └── utils.py         # PDF analysis utilities
├── data/                    # Example PDFs directory
│   ├── academic_paper_figure.pdf
│   ├── attention_paper.pdf
│   └── ...
├── requirements.txt         # Project dependencies
└── README.md               # Project documentation
```

### Adding Example PDFs

1. Place your example PDFs in the `data` directory
2. The application will automatically detect and list them in the examples section

## Limitations

- Maximum of 5 consecutive pages can be processed at once
- Some parsers may have specific limitations:
  - PyPDF2: Basic text extraction, may struggle with complex layouts
  - PDFMiner: Slower processing but better layout preservation
  - PyMuPDF: Requires additional system dependencies
  - Docling: Demo implementation only

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
