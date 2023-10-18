"""An abstract base class for ingesting different types of quote files."""

from abc import ABC, abstractmethod
from typing import List
from QuoteEngine.QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """
    Abstract base class.

    Attributes:
        None

    Methods:
        can_ingest(cls, path: str) -> bool:
            Check if the class can ingest the given file.

        parse(cls, path: str) -> List[QuoteModel]:
            Parse the given file and return a list of QuoteModel objects.
    """

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if the class can ingest the given file.

        :param path: The path to the file to be ingested.
        :return: True if the class can ingest the file, False otherwise.
        """
        pass

    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the given file and return a list of QuoteModel objects.

        :param path: The path to the file to be parsed.
        :return: A list of QuoteModel objects parsed from the file.
        """
        pass
