import os
import traceback

from loguru import logger

from .base_parser import PDFParser


class PyMuPDFParser(PDFParser):
    """
    PDF parser implementation using PyMuPDF (fitz).
    """

    @property
    def name(self):
        return "PyMuPDF"

    @property
    def description(self):
        return (
            "PyMuPDF is a Python binding for MuPDF, which is a lightweight PDF and XPS viewer. "
            "It's fast and provides good quality text extraction with formatting preservation."
        )

    @property
    def link(self):
        return "https://pymupdf.readthedocs.io/"

    def extract_text(self, file_path, start_page, max_pages):
        """
        Extract text from a PDF file using PyMuPDF.

        Args:
            file_path (str): Path to the PDF file
            start_page (int): Page to start extraction from (1-indexed)
            max_pages (int): Maximum number of pages to extract

        Returns:
            str: Extracted text in markdown format
        """
        try:
            # Import here to avoid errors if PyMuPDF is not installed
            import fitz  # PyMuPDF

            logger.info(f"Opening PDF document: {file_path}")

            # Check if file exists and can be read
            if not os.path.isfile(file_path):
                logger.error(f"File not found: {file_path}")
                return f"# Error\n\nFile not found: {file_path}"

            # Try to get file info before opening it fully
            try:
                file_size = os.path.getsize(file_path)
                logger.info(f"File size: {file_size} bytes")
                if file_size == 0:
                    logger.error("Empty PDF file detected (0 bytes)")
                    return "# Error\n\nEmpty PDF file detected (0 bytes)."
            except Exception as e:
                logger.warning(f"Could not check file size: {str(e)}")

            # Verify file is readable
            try:
                with open(file_path, "rb") as f:
                    header = f.read(5)
                    if header != b"%PDF-":
                        logger.error(
                            "Invalid PDF file: File does not begin with %PDF- header"
                        )
                        return "# Error\n\nInvalid PDF file: File does not begin with %PDF- header."
            except Exception as e:
                logger.error(f"Cannot read file: {str(e)}")
                return f"# Error\n\nCannot read file: {str(e)}"

            # Attempt to open the document with detailed logging
            try:
                doc = fitz.open(file_path)
                logger.info(
                    f"Successfully opened document. Page count: {doc.page_count}"
                )
            except Exception as e:
                detailed_error = traceback.format_exc()
                logger.error(
                    f"PyMuPDF could not open the document: {str(e)}\n{detailed_error}"
                )
                return f"# Error\n\nPyMuPDF could not open the document: {str(e)}\n\n```\n{detailed_error}\n```"

            # Calculate page range (convert from 1-indexed to 0-indexed)
            start_idx = start_page - 1
            end_idx = min(start_idx + max_pages, doc.page_count)

            if start_idx >= doc.page_count:
                doc.close()
                logger.error(
                    f"Start page ({start_page}) exceeds document length ({doc.page_count} pages)"
                )
                return f"# Error\n\nStart page ({start_page}) exceeds document length ({doc.page_count} pages)."

            logger.info(
                f"Extracting text from pages {start_page} to {min(start_page + max_pages - 1, doc.page_count)}"
            )

            text = "# Document Analysis with PyMuPDF\n\n"
            text += "## Document Information\n\n"

            # Add document metadata if available
            if doc.metadata:
                text += "### Metadata\n\n"
                for key, value in doc.metadata.items():
                    if value:  # Only add non-empty values
                        text += f"- **{key}**: {value}\n"
                text += "\n"

            # Extract text page by page with detailed logging
            text += "## Extracted Text\n\n"
            for i in range(start_idx, end_idx):
                try:
                    logger.info(f"Processing page {i+1}")
                    page = doc[i]

                    # Use plain text format instead of markdown (which isn't directly supported)
                    # According to docs, we should use PyMuPDF4LLM for proper markdown conversion
                    try:
                        page_text = page.get_text("text")
                        logger.debug("Successfully extracted text with 'text' format")
                    except Exception as text_error:
                        logger.error(
                            f"Error extracting text with 'text' format: {str(text_error)}"
                        )
                        # Try alternative formats if 'text' fails
                        try:
                            page_text = page.get_text()  # Default format
                            logger.debug(
                                "Successfully extracted text with default format"
                            )
                        except Exception as default_error:
                            logger.error(
                                f"Error extracting text with default format: {str(default_error)}"
                            )
                            page_text = "*Could not extract text from this page due to format errors*"

                    # Check if we got any text
                    if not page_text.strip():
                        logger.warning(f"No text extracted from page {i+1}")
                        page_text = "*No text could be extracted from this page.*"

                    # Format as markdown by wrapping in code block for better readability
                    text += f"### Page {i+1}\n\n```\n{page_text}\n```\n\n"
                except Exception as e:
                    detailed_error = traceback.format_exc()
                    logger.error(
                        f"Error extracting text from page {i+1}: {str(e)}\n{detailed_error}"
                    )
                    text += f"### Page {i+1}\n\n*Error extracting text: {str(e)}*\n\n"

            # Try to extract images if possible (not always available)
            try:
                image_count = 0
                for i in range(start_idx, end_idx):
                    page = doc[i]
                    image_list = page.get_images()
                    image_count += len(image_list)

                if image_count > 0:
                    text += "## Images\n\n"
                    text += f"The document contains approximately {image_count} images in the selected pages.\n\n"
            except Exception as e:
                logger.error(f"Error counting images: {str(e)}")

            doc.close()
            logger.success("PyMuPDF extraction completed successfully")
            return text

        except ImportError:
            logger.error("PyMuPDF (fitz) is not installed")
            return "# Error\n\nPyMuPDF (fitz) is not installed. Install with: `pip install pymupdf`"
        except Exception as e:
            detailed_error = traceback.format_exc()
            logger.error(
                f"Unexpected error in PyMuPDF parser: {str(e)}\n{detailed_error}"
            )
            return f"# Error\n\nFailed to extract text with PyMuPDF: {str(e)}\n\n```\n{detailed_error}\n```"
