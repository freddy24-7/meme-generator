"""A class for ingesting quotes from DOCX files."""

from typing import List
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.IngestorInterface import IngestorInterface
import docx


class DocxIngestor(IngestorInterface):
    """
    DOCX files Ingestor class.

    Methods:
        can_ingest(cls, path: str) -> bool:
            Check if the class can ingest the given DOCX file.

        parse(cls, path: str) -> List[QuoteModel]:
            Parse the given DOCX file and return a list of QuoteModel objects.
    """

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the class can ingest the given DOCX file.

        :param path: The path to the DOCX file to be ingested.
        :return: True if the class can ingest the DOCX file, False otherwise.
        """
        return path.endswith('.docx')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the given DOCX file and return a list of QuoteModel objects.

        :param path: The path to the DOCX file to be parsed.
        :return: A list of QuoteModel objects parsed from the DOCX file.
        """
        quotes = []
        doc = docx.Document(path)
        for paragraph in doc.paragraphs:
            text = paragraph.text.strip()
            if text:
                parts = text.split(' - ')
                if len(parts) == 2:
                    body, author = parts
                    quote = QuoteModel(body, author)
                    quotes.append(quote)
        return quotes
