# PDF Parsers Playground (PPP)

A Streamlit application that allows you to experiment with various PDF parsing libraries. This app mimics the interface shown in the reference images, providing functionality to upload, preview, and convert PDFs using different parsing methods.

## Features

- **Upload Section**: Upload your own PDF documents
- **Examples Section**: Select from pre-populated example PDFs
- **PDF Preview**: View the uploaded or selected PDF
- **Conversion Methods**: Choose from various PDF parsing libraries
- **Advanced Settings**: Configure starting page and enable debug visualization
- **Result Tabs**: View results as rendered markdown, raw text, debug visualization, and library information

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run pdf_playground_app.py
```

## Supported PDF Parsers

- **PyMuPDF**: A Python binding for MuPDF, which is a lightweight PDF and XPS viewer
- **PyPDF2**: A pure-Python PDF library capable of splitting, merging, cropping, and transforming PDF files
- **PDFMiner**: A tool for extracting information from PDF documents
- **Docling**: (Demo purposes only) A fictional PDF parser

## Project Structure

```
pdf-parsers-playground/
├── pdf_playground_app.py     # Main Streamlit application
├── requirements.txt          # Required Python dependencies
├── data/                     # Directory to store example PDFs
│   ├── academic_paper_figure.pdf
│   ├── attention_paper.pdf
│   └── ...
└── README.md                 # This file
```

## Extending the App

To add more PDF parsers:

1. Install the required library
2. Add the parser to the `parser_info` dictionary in the main application
3. Implement an extraction function for the new parser

## Limitations

- The app currently supports processing a maximum of 5 consecutive pages
- Example PDFs need to be manually added to the data directory
- Some parsers may require additional dependencies