"""This class encapsulates a quote's body."""


class QuoteModel:
    """
    Represents a quote with a body and an author.

    Attributes:
        body (str): The text of the quote.
        author (str): The author of the quote.

    Methods:
        __init__(self, body: str, author: str):
            Initialize a QuoteModel object with a quote body and author.

        __str__(self) -> str:
            Return a string representation of the quote in the format:
            "{quote body}", {author}
    """

    def __init__(self, body: str, author: str):
        """
        Initialize a QuoteModel object with a quote body and author.

        Args:
            body (str): The text of the quote.
            author (str): The author of the quote.
        """
        self.body = body
        self.author = author

    def __str__(self) -> str:
        """
        Return a string representation of the quote.

        Returns:
            str: A string in the format: "{quote body}", {author}
        """
        return f'"{self.body}", {self.author}'
