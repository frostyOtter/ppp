"""
PDF Parsers Package

This package contains implementations of various PDF parsing libraries.
"""

from loguru import logger

from .pymupdf_parser import PyMuPDFParser
from .pypdf2_parser import PyPDF2Parser
from .pdfminer_parser import PDFMinerParser
from .docling_parser import DoclingParser
from .utils import pdf_diagnostic_info, analyze_pdf_structure

# Create instances of all parsers
parsers = {
    "PyMuPDF": PyMuPDFParser(),
    "PyPDF2": PyPDF2Parser(),
    "PDFMiner": PDFMinerParser(),
    "Docling": DoclingParser(),
}

# Log available parsers
logger.info(f"Initialized PDF parsers: {', '.join(parsers.keys())}")


# Function to get all available parsers
def get_available_parsers():
    """
    Returns a dictionary of all available parsers.

    Returns:
        dict: A dictionary mapping parser names to parser instances
    """
    return parsers


# Function to get a specific parser by name
def get_parser(name):
    """
    Get a parser by name.

    Args:
        name (str): The name of the parser

    Returns:
        PDFParser: The parser instance if found, None otherwise
    """
    parser = parsers.get(name)
    if parser:
        logger.info(f"Retrieved parser: {name}")
    else:
        logger.warning(f"Parser not found: {name}")
    return parser


# Export the names of all available parsers and utilities
__all__ = [
    "PyMuPDFParser",
    "PyPDF2Parser",
    "PDFMinerParser",
    "DoclingParser",
    "get_available_parsers",
    "get_parser",
    "pdf_diagnostic_info",
    "analyze_pdf_structure",
]
