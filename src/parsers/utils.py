import os
import platform
import sys
import tempfile
from pathlib import Path

from loguru import logger


def pdf_diagnostic_info(file_path):
    """
    Gather diagnostic information about a PDF file and system environment.

    Args:
        file_path (str): Path to the PDF file

    Returns:
        str: Formatted diagnostic information
    """
    info = []
    info.append("# PDF Diagnostic Information\n")

    # System information
    info.append("## System Information\n")
    info.append(f"- **OS**: {platform.system()} {platform.release()}\n")
    info.append(f"- **Python Version**: {sys.version.split()[0]}\n")

    # Check for common PDF libraries
    info.append("\n## Installed PDF Libraries\n")

    try:
        import fitz

        info.append(f"- **PyMuPDF**: {fitz.__version__}\n")
    except ImportError:
        info.append("- **PyMuPDF**: Not installed\n")

    try:
        import PyPDF2

        info.append(f"- **PyPDF2**: {PyPDF2.__version__}\n")
    except ImportError:
        info.append("- **PyPDF2**: Not installed\n")

    try:
        import pdfminer

        info.append(f"- **PDFMiner**: {getattr(pdfminer, '__version__', 'Unknown')}\n")
    except ImportError:
        info.append("- **PDFMiner**: Not installed\n")

    # File information
    if file_path and os.path.exists(file_path):
        info.append("\n## File Information\n")
        try:
            file_size = os.path.getsize(file_path)
            info.append(f"- **Path**: {file_path}\n")
            info.append(f"- **Size**: {file_size} bytes ({file_size/1024:.2f} KB)\n")
            info.append(f"- **Last Modified**: {os.path.getmtime(file_path)}\n")

            # Check file permissions
            permissions = ""
            if os.access(file_path, os.R_OK):
                permissions += "r"
            if os.access(file_path, os.W_OK):
                permissions += "w"
            if os.access(file_path, os.X_OK):
                permissions += "x"
            info.append(f"- **Permissions**: {permissions}\n")

            # Check file header to confirm it's a PDF
            with open(file_path, "rb") as f:
                header = f.read(10)
                is_pdf = header.startswith(b"%PDF-")
                info.append(f"- **Valid PDF Header**: {'Yes' if is_pdf else 'No'}\n")

                if is_pdf:
                    # Get PDF version
                    version = header[5:8].decode("ascii", errors="ignore")
                    info.append(f"- **PDF Version**: {version}\n")

        except Exception as e:
            logger.error(f"Error reading file info: {e}")
            info.append(f"- **Error Reading File**: {str(e)}\n")
    else:
        info.append("\n## File Information\n")
        info.append(f"- **Path**: {file_path}\n")
        info.append("- **Status**: File not found or not accessible\n")

    return "".join(info)


def analyze_pdf_structure(file_path):
    """
    Attempt to analyze the internal structure of a PDF file using multiple libraries.

    Args:
        file_path (str): Path to the PDF file

    Returns:
        str: Analysis results in markdown format
    """
    result = []
    result.append("# PDF Structure Analysis\n\n")

    if not os.path.exists(file_path):
        return result[0] + "File not found or not accessible."

    # Try PyMuPDF (fitz) first
    result.append("## PyMuPDF Analysis\n\n")
    try:
        import fitz

        doc = fitz.open(file_path)

        # Basic document information
        result.append(f"- **Page Count**: {doc.page_count}\n")
        result.append(f"- **Metadata**: {bool(doc.metadata)}\n")
        result.append(f"- **Is Encrypted**: {doc.is_encrypted}\n")
        result.append(f"- **Is Repaired**: {doc.is_repaired}\n")

        # Page structure summary
        if doc.page_count > 0:
            result.append("\n### First Page Analysis\n\n")
            page = doc[0]
            result.append(f"- **Rotation**: {page.rotation} degrees\n")
            result.append(
                f"- **Size**: {page.rect.width:.1f} x {page.rect.height:.1f} points\n"
            )

            # Count text blocks and images
            try:
                blocks = page.get_text("dict")["blocks"]
                text_blocks = sum(1 for b in blocks if b["type"] == 0)
                image_blocks = sum(1 for b in blocks if b["type"] == 1)
                result.append(f"- **Text Blocks**: {text_blocks}\n")
                result.append(f"- **Image Blocks**: {image_blocks}\n")
            except Exception as e:
                logger.error(f"Error analyzing blocks: {e}")
                result.append(f"- **Block Analysis Error**: {str(e)}\n")

        doc.close()

    except ImportError:
        result.append("PyMuPDF not installed.\n\n")
    except Exception as e:
        logger.error(f"PyMuPDF analysis error: {e}")
        result.append(f"PyMuPDF analysis error: {str(e)}\n\n")

    # Try PyPDF2
    result.append("\n## PyPDF2 Analysis\n\n")
    try:
        import PyPDF2

        with open(file_path, "rb") as file:
            try:
                reader = PyPDF2.PdfReader(file)
                result.append(f"- **Page Count**: {len(reader.pages)}\n")
                result.append(f"- **Is Encrypted**: {reader.is_encrypted}\n")

                # Document info
                if reader.metadata:
                    result.append("- **Has Metadata**: Yes\n")
                    # Sample a few metadata fields
                    for key in ["/Title", "/Author", "/Producer"]:
                        if key in reader.metadata:
                            result.append(f"  - {key}: Present\n")
                else:
                    result.append("- **Has Metadata**: No\n")

                # Check document structure
                if len(reader.pages) > 0:
                    result.append("\n### First Page Analysis\n\n")
                    page = reader.pages[0]
                    result.append(f"- **Page Size**: {page.mediabox}\n")
                    result.append(f"- **Rotation**: {page.get('/Rotate', 0)}\n")

                    # Check if text extraction works
                    try:
                        text = page.extract_text()
                        result.append(
                            f"- **Text Extraction**: {'Successful' if text else 'No text found'}\n"
                        )
                        result.append(f"- **Text Length**: {len(text)} characters\n")
                    except Exception as e:
                        logger.error(f"Text extraction error: {e}")
                        result.append(f"- **Text Extraction Error**: {str(e)}\n")

            except PyPDF2.errors.PdfReadError as e:
                logger.error(f"PyPDF2 read error: {e}")
                result.append(f"PyPDF2 can't read this file: {str(e)}\n")
            except Exception as e:
                logger.error(f"PyPDF2 general error: {e}")
                result.append(f"PyPDF2 analysis error: {str(e)}\n")

    except ImportError:
        result.append("PyPDF2 not installed.\n\n")
    except Exception as e:
        logger.error(f"PyPDF2 import error: {e}")
        result.append(f"PyPDF2 analysis error: {str(e)}\n\n")

    return "".join(result)
