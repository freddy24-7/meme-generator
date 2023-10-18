"""A class for ingesting quotes from PDF files."""

from typing import List
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.IngestorInterface import IngestorInterface
import subprocess
import tempfile
import os
import re


class PDFIngestor(IngestorInterface):
    """
    PDF files ingestor.

    Methods:
        can_ingest(cls, path: str) -> bool:
            Check if the class can ingest the given PDF file.

        parse(cls, path: str) -> List[QuoteModel]:
            Parse the given PDF file and return a list of QuoteModel objects.
    """

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the class can ingest the given PDF file.

        :param path: The path to the PDF file to be ingested.
        :return: True if the class can ingest the PDF file, False otherwise.
        """
        return path.endswith('.pdf')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the given PDF file and return a list of QuoteModel objects.

        :param path: The path to the PDF file to be parsed.
        :return: A list of QuoteModel objects parsed from the PDF file.
        """
        quotes = []
        try:
            with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as temp_file:
                subprocess.run(["pdftotext", "-layout", path, temp_file.name])
                temp_file.seek(0)
                pdf_text = temp_file.read().decode('utf-8')

            lines = pdf_text.strip().split('\n')
            for line in lines:
                match = re.match(r'"([^"]*)" - ([^"]*)', line.strip())
                if match:
                    body = match.group(1)
                    author = match.group(2)
                    quote = QuoteModel(body, author)
                    quotes.append(quote)
            os.remove(temp_file.name)
        except Exception as e:
            print(f"Error: {e}")
        return quotes
