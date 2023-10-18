"""A class for ingesting quotes from various file formats."""

from typing import List
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.CSVIngestor import CSVIngestor
from QuoteEngine.PDFIngestor import PDFIngestor
from QuoteEngine.DocxIngestor import DocxIngestor
from QuoteEngine.TextIngestor import TextIngestor
from QuoteEngine.IngestorInterface import IngestorInterface


class Ingestor(IngestorInterface):
    """
    Ingestor class.

    This class provides a common interface for ingesting quotes from multiple
    file formats, including CSV, PDF, DOCX, and TXT.

    Attributes:
        ingestors (List[IngestorInterface]): A list of ingestor classes to
            handle specific file formats.

    Methods:
        can_ingest(cls, path: str) -> bool:
            Check if any of the registered ingestors can ingest the given file.

        parse(cls, path: str) -> List[QuoteModel]:
            Parse a file and extract quotes using the appropriate ingestor.
    """

    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if any of the registered ingestors can ingest the given file.

        Args:
            path (str): The file path to check.

        Returns:
            bool: True if any of the ingestors can handle the file format;
                  False otherwise.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return True
        return False

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a file and extract quotes using the appropriate ingestor.

        Args:
            path (str): The file path of the file to parse.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects representing the parsed quotes.

        Raises:
            Exception: If no supported ingestor is found for the file format.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise Exception("Unsupported file format")
