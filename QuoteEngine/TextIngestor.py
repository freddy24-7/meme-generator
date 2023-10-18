"""A class for ingesting quotes from text files."""

from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.IngestorInterface import IngestorInterface
from typing import List


class TextIngestor(IngestorInterface):
    """
    This class implements the IngestorInterface.

    It can parse text files to extract quotes.

    Attributes:
        None

    Methods:
        can_ingest(cls, path: str) -> bool:
            Check if the given file path can be ingested by this class.

        parse(cls, path: str) -> List[QuoteModel]:
            Parse a text file and extract quotes as a list of QuoteModel objects.

    """

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the given file path can be ingested by this class.

        Args:
            path (str): The file path to check.

        Returns:
            bool: True if the file has a '.txt' extension, indicating it can be ingested;
                  False otherwise.
        """
        return path.endswith('.txt')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a text file and extract quotes as a list of QuoteModel objects.

        Args:
            path (str): The file path of the text file to parse.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects representing the parsed quotes.
        """
        quotes = []
        try:
            with open(path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(' - ')
                    if len(parts) == 2:
                        body, author = parts
                        quote = QuoteModel(body, author)
                        quotes.append(quote)
        except Exception as e:
            print(f"Error: {e}")

        return quotes
