"""Aclass for ingesting quotes from CSV files."""

from typing import List
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.IngestorInterface import IngestorInterface
import pandas as pd


class CSVIngestor(IngestorInterface):
    """
    CSV Ingestor class.

    Methods:
        can_ingest(cls, path: str) -> bool:
            Check if the class can ingest the given CSV file.

        parse(cls, path: str) -> List[QuoteModel]:
            Parse the given CSV file and return a list of QuoteModel objects.
    """

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the class can ingest the given CSV file.

        :param path: The path to the CSV file to be ingested.
        :return: True if the class can ingest the CSV file, False otherwise.
        """
        return path.endswith('.csv')

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the given CSV file and return a list of QuoteModel objects.

        :param path: The path to the CSV file to be parsed.
        :return: A list of QuoteModel objects parsed from the CSV file.
        """
        quotes = []
        try:
            df = pd.read_csv(path)
            for index, row in df.iterrows():
                body = row['body']
                author = row['author']
                quote = QuoteModel(body, author)
                quotes.append(quote)
        except Exception as e:
            print(f"Error: {e}")
        return quotes
