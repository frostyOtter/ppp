from .base_parser import PDFParser
import traceback

from loguru import logger


class PDFMinerParser(PDFParser):
    """
    PDF parser implementation using PDFMiner.Six.
    """

    @property
    def name(self):
        return "PDFMiner"

    @property
    def description(self):
        return (
            "PDFMiner is a tool for extracting information from PDF documents. "
            "It focuses on getting and analyzing text data and provides detailed control over extraction parameters."
        )

    @property
    def link(self):
        return "https://github.com/pdfminer/pdfminer.six"

    def extract_text(self, file_path, start_page, max_pages):
        """
        Extract text from a PDF file using PDFMiner.

        Args:
            file_path (str): Path to the PDF file
            start_page (int): Page to start extraction from (1-indexed)
            max_pages (int): Maximum number of pages to extract

        Returns:
            str: Extracted text in markdown format
        """
        try:
            # Import here to avoid errors if PDFMiner is not installed
            from pdfminer.high_level import extract_text
            from pdfminer.pdfpage import PDFPage
            from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
            from pdfminer.converter import TextConverter
            from pdfminer.layout import LAParams
            import io

            logger.info(f"Opening PDF with PDFMiner: {file_path}")

            # Get page count for validation
            page_count = 0
            try:
                with open(file_path, "rb") as fp:
                    page_count = sum(1 for _ in PDFPage.get_pages(fp))
                logger.info(f"Document has {page_count} pages")
            except Exception as e:
                logger.error(f"Error counting pages: {str(e)}")
                return f"# Error\n\nFailed to count pages in PDF: {str(e)}"

            # Calculate page range (convert from 1-indexed to 0-indexed)
            start_idx = start_page - 1
            end_idx = start_idx + max_pages

            if start_idx >= page_count:
                logger.error(
                    f"Start page ({start_page}) exceeds document length ({page_count} pages)"
                )
                return f"# Error\n\nStart page ({start_page}) exceeds document length ({page_count} pages)."

            end_idx = min(end_idx, page_count)
            page_numbers = list(range(start_idx, end_idx))

            logger.info(
                f"Extracting text from pages {start_page} to {min(start_page + max_pages - 1, page_count)}"
            )

            text = f"# Document Analysis with PDFMiner\n\n"
            text += f"## Document Information\n\n"
            text += f"- **Total Pages**: {page_count}\n\n"

            # Extract text page by page
            text += "## Extracted Text\n\n"
            for page_num in page_numbers:
                try:
                    logger.info(f"Processing page {page_num+1}")

                    # Extract text for each page separately
                    output_string = io.StringIO()
                    with open(file_path, "rb") as fp:
                        resource_manager = PDFResourceManager()
                        device = TextConverter(
                            resource_manager, output_string, laparams=LAParams()
                        )
                        interpreter = PDFPageInterpreter(resource_manager, device)

                        # Skip to the desired page
                        for i, page in enumerate(PDFPage.get_pages(fp)):
                            if i == page_num:
                                logger.debug(
                                    f"Found page {page_num+1}, extracting text"
                                )
                                interpreter.process_page(page)
                                break

                    page_text = output_string.getvalue()

                    # Check if we got any text
                    if not page_text.strip():
                        logger.warning(f"No text extracted from page {page_num+1}")
                        page_text = "*No text could be extracted from this page.*"

                    text += f"### Page {page_num+1}\n\n```\n{page_text}\n```\n\n"

                except Exception as e:
                    detailed_error = traceback.format_exc()
                    logger.error(
                        f"Error extracting text from page {page_num+1}: {str(e)}\n{detailed_error}"
                    )
                    text += f"### Page {page_num+1}\n\n*Error extracting text: {str(e)}*\n\n"

            logger.success("PDFMiner extraction completed successfully")
            return text

        except ImportError:
            logger.error("PDFMiner is not installed")
            return "# Error\n\nPDFMiner is not installed. Install with: `pip install pdfminer.six`"
        except Exception as e:
            detailed_error = traceback.format_exc()
            logger.error(
                f"Unexpected error in PDFMiner parser: {str(e)}\n{detailed_error}"
            )
            return f"# Error\n\nFailed to extract text with PDFMiner: {str(e)}\n\n```\n{detailed_error}\n```"
