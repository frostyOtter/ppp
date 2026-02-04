import traceback

from loguru import logger

from .base_parser import PDFParser


class PyPDF2Parser(PDFParser):
    """
    PDF parser implementation using PyPDF2.
    """

    @property
    def name(self):
        return "PyPDF2"

    @property
    def description(self):
        return (
            "PyPDF2 is a pure-Python PDF library capable of splitting, merging, cropping, and transforming PDF files. "
            "It's reliable for basic text extraction but may struggle with complex layouts."
        )

    @property
    def link(self):
        return "https://pypdf2.readthedocs.io/"

    def parse(self, file_path, start_page, max_pages):
        """
        Extract text from a PDF file using PyPDF2.

        Args:
            file_path (str): Path to the PDF file
            start_page (int): Page to start extraction from (1-indexed)
            max_pages (int): Maximum number of pages to extract

        Returns:
            str: Extracted text in markdown format
        """
        try:
            # Import here to avoid errors if PyPDF2 is not installed
            import pypdf as PyPDF2

            logger.info(f"Opening PDF with PyPDF2: {file_path}")

            with open(file_path, "rb") as file:
                try:
                    reader = PyPDF2.PdfReader(file)
                    logger.info(
                        f"Successfully opened document. Page count: {len(reader.pages)}"
                    )

                    # Calculate page range (convert from 1-indexed to 0-indexed)
                    start_idx = start_page - 1
                    end_idx = min(start_idx + max_pages, len(reader.pages))

                    if start_idx >= len(reader.pages):
                        logger.error(
                            f"Start page ({start_page}) exceeds document length ({len(reader.pages)} pages)"
                        )
                        return f"# Error\n\nStart page ({start_page}) exceeds document length ({len(reader.pages)} pages)."

                    logger.info(
                        f"Extracting text from pages {start_page} to {min(start_page + max_pages - 1, len(reader.pages))}"
                    )

                    text = "# Document Analysis with PyPDF2\n\n"
                    text += "## Document Information\n\n"
                    text += f"- **Total Pages**: {len(reader.pages)}\n"
                    text += (
                        f"- **Encrypted**: {'Yes' if reader.is_encrypted else 'No'}\n\n"
                    )

                    # Add document metadata if available
                    if reader.metadata:
                        text += "### Metadata\n\n"
                        for key, value in reader.metadata.items():
                            if value:  # Only add non-empty values
                                text += f"- **{key}**: {value}\n"
                        text += "\n"

                    # Extract text page by page
                    text += "## Extracted Text\n\n"
                    for i in range(start_idx, end_idx):
                        try:
                            logger.info(f"Processing page {i+1}")
                            page = reader.pages[i]
                            page_text = page.extract_text()

                            # Check if we got any text
                            if not page_text.strip():
                                logger.warning(f"No text extracted from page {i+1}")
                                page_text = (
                                    "*No text could be extracted from this page.*"
                                )

                            # Convert to markdown-friendly format
                            text += f"### Page {i+1}\n\n```\n{page_text}\n```\n\n"
                        except Exception as e:
                            detailed_error = traceback.format_exc()
                            logger.error(
                                f"Error extracting text from page {i+1}: {str(e)}\n{detailed_error}"
                            )
                            text += f"### Page {i+1}\n\n*Error extracting text: {str(e)}*\n\n"

                    logger.success("PyPDF2 extraction completed successfully")
                    return text

                except PyPDF2.errors.PdfReadError as e:
                    logger.error(f"PyPDF2 read error: {str(e)}")
                    return f"# Error\n\nPyPDF2 could not read this PDF: {str(e)}"
                except Exception as e:
                    detailed_error = traceback.format_exc()
                    logger.error(
                        f"Error during PyPDF2 processing: {str(e)}\n{detailed_error}"
                    )
                    return f"# Error\n\nFailed to process PDF with PyPDF2: {str(e)}\n\n```\n{detailed_error}\n```"

        except ImportError:
            logger.error("PyPDF2 is not installed")
            return (
                "# Error\n\nPyPDF2 is not installed. Install with: `pip install PyPDF2`"
            )
        except Exception as e:
            detailed_error = traceback.format_exc()
            logger.error(
                f"Unexpected error in PyPDF2 parser: {str(e)}\n{detailed_error}"
            )
            return f"# Error\n\nFailed to extract text with PyPDF2: {str(e)}\n\n```\n{detailed_error}\n```"
