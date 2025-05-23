from abc import ABC, abstractmethod


class PDFParser(ABC):
    """
    Abstract base class for PDF parsers.
    All parser implementations should inherit from this class.
    """

    @property
    @abstractmethod
    def name(self):
        """Return the name of the parser."""
        pass

    @property
    @abstractmethod
    def description(self):
        """Return a description of the parser."""
        pass

    @property
    @abstractmethod
    def link(self):
        """Return a link to the parser's documentation or homepage."""
        pass

    @abstractmethod
    def extract_text(self, file_path, start_page, max_pages):
        """
        Extract text from a PDF file.

        Args:
            file_path (str): Path to the PDF file
            start_page (int): Page to start extraction from (1-indexed)
            max_pages (int): Maximum number of pages to extract

        Returns:
            str: Extracted text in markdown format
        """
        pass
