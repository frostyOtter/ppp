import os
import tempfile
import traceback
from pathlib import Path

from loguru import logger

from .base_parser import PDFParser


class DoclingParser(PDFParser):
    """
    PDF parser implementation using Docling.

    Docling is specialized in structured document understanding with capabilities
    for extracting tables, text, and maintaining document layout.
    """

    @property
    def name(self):
        return "Docling"

    @property
    def description(self):
        return (
            "Docling is a PDF parser specialized in document understanding and table extraction. "
            "It can identify and extract tables from documents while preserving their structure, "
            "and export them to various formats like CSV, HTML, and Pandas DataFrames."
        )

    @property
    def link(self):
        return "https://github.com/example/docling"  # Replace with actual link when available

    def extract_text(self, file_path, start_page, max_pages):
        """
        Extract text and tables from a PDF file using Docling.

        Args:
            file_path (str): Path to the PDF file
            start_page (int): Page to start extraction from (1-indexed)
            max_pages (int): Maximum number of pages to extract

        Returns:
            str: Extracted text in markdown format with tables
        """
        try:
            # Import Docling (will raise ImportError if not installed)
            try:
                from docling.document_converter import DocumentConverter

                logger.info("Successfully imported Docling")
            except ImportError:
                logger.error("Docling is not installed")
                return "# Error\n\nDocling is not installed. Install with: `pip install docling`"

            # Create output directory for any extracted tables
            temp_dir = tempfile.mkdtemp()
            output_dir = Path(temp_dir)
            logger.info(f"Created temporary directory for outputs: {temp_dir}")

            # Initialize the converter
            doc_converter = DocumentConverter()

            # Convert the document
            logger.info(f"Converting document: {file_path}")
            try:
                conv_res = doc_converter.convert(
                    file_path,
                    page_numbers=list(
                        range(start_page - 1, start_page - 1 + max_pages)
                    ),
                )
                logger.info("Document conversion successful")
            except Exception as e:
                detailed_error = traceback.format_exc()
                logger.error(f"Error converting document: {str(e)}\n{detailed_error}")
                return f"# Error\n\nFailed to convert document with Docling: {str(e)}\n\n```\n{detailed_error}\n```"

            # Get the document filename without extension
            doc_filename = Path(file_path).stem

            # Start building the markdown output
            markdown_output = f"# Document Analysis: {doc_filename}\n\n"

            # Add document metadata if available
            if hasattr(conv_res.document, "metadata") and conv_res.document.metadata:
                logger.info("Adding document metadata")
                markdown_output += "## Document Metadata\n\n"
                for key, value in conv_res.document.metadata.items():
                    markdown_output += f"- **{key}**: {value}\n"
                markdown_output += "\n"

            # Add document text
            markdown_output += "## Document Text\n\n"

            # Add text by page
            current_page = start_page
            for page in conv_res.document.pages:
                if current_page > start_page + max_pages - 1:
                    break

                logger.info(f"Processing page {current_page}")
                markdown_output += f"### Page {current_page}\n\n"

                # Add text blocks for this page
                for text_block in page.text_blocks:
                    markdown_output += f"{text_block.text}\n\n"

                current_page += 1

            # Add tables section if tables are present
            if conv_res.document.tables:
                logger.info(f"Found {len(conv_res.document.tables)} tables in document")
                markdown_output += "## Extracted Tables\n\n"

                # Process each table
                for table_ix, table in enumerate(conv_res.document.tables):
                    logger.info(f"Processing table {table_ix + 1}")
                    markdown_output += f"### Table {table_ix + 1}\n\n"

                    # Convert table to DataFrame and then to markdown
                    try:
                        table_df = table.export_to_dataframe()
                        markdown_output += table_df.to_markdown() + "\n\n"

                        # Save the table to files in the temp directory
                        csv_filename = (
                            output_dir / f"{doc_filename}-table-{table_ix + 1}.csv"
                        )
                        html_filename = (
                            output_dir / f"{doc_filename}-table-{table_ix + 1}.html"
                        )

                        logger.info(f"Saving CSV table to {csv_filename}")
                        table_df.to_csv(csv_filename)

                        logger.info(f"Saving HTML table to {html_filename}")
                        with html_filename.open("w") as fp:
                            fp.write(table.export_to_html(doc=conv_res.document))

                        markdown_output += f"*Table {table_ix + 1} has been saved as CSV and HTML.*\n\n"
                    except Exception as e:
                        detailed_error = traceback.format_exc()
                        logger.error(
                            f"Error processing table {table_ix + 1}: {str(e)}\n{detailed_error}"
                        )
                        markdown_output += (
                            f"*Error processing table {table_ix + 1}: {str(e)}*\n\n"
                        )

            # Add information about images if available
            if hasattr(conv_res.document, "images") and conv_res.document.images:
                logger.info(f"Found {len(conv_res.document.images)} images in document")
                markdown_output += "## Images\n\n"
                markdown_output += (
                    f"The document contains {len(conv_res.document.images)} images.\n\n"
                )

            logger.success("Docling extraction completed successfully")
            return markdown_output

        except Exception as e:
            detailed_error = traceback.format_exc()
            logger.error(
                f"Unexpected error in Docling parser: {str(e)}\n{detailed_error}"
            )
            return f"# Error\n\nFailed to extract text with Docling: {str(e)}\n\n```\n{detailed_error}\n```"
        finally:
            # Clean up temporary files
            if "temp_dir" in locals() and os.path.exists(temp_dir):
                import shutil

                logger.info(f"Cleaning up temporary directory: {temp_dir}")
                try:
                    shutil.rmtree(temp_dir)
                except Exception as e:
                    logger.error(f"Error cleaning up temporary directory: {str(e)}")
