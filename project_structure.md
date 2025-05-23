pdf_parsers_playground/
├── main.py                  # Main Streamlit application
├── requirements.txt         # Required dependencies
├── README.md                # Project documentation
├── data/                    # Directory for example PDFs
│   ├── academic_paper_figure.pdf
│   ├── attention_paper.pdf
│   └── ...
└── parsers/                 # Directory for parser modules
    ├── __init__.py          # Makes parsers a proper package
    ├── base_parser.py       # Abstract base class for parsers
    ├── pymupdf_parser.py    # PyMuPDF implementation
    ├── docling_parser.py    # Docling implementation
    ├── pypdf2_parser.py     # PyPDF2 implementation
    └── pdfminer_parser.py   # PDFMiner implementation
    ...                     # Other parser implementations