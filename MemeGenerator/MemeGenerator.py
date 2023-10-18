"""Generates memes by adding text captions to images."""

import os
import random
from PIL import Image, ImageDraw, ImageFont


class MemeGenerator:
    """
    This class allows the generation of memes.

    This happens by adding text captions to
    existing images. It resizes the image to a specified width, adds a caption
    with a specified font and random position, and saves the resulting meme
    image to an output directory.

    Attributes:
        DEFAULT_FONT_SIZE (int): The default font size for the caption text.

    Methods:
        __init__(self, output_dir: str, font: str):
            Initialize a MemeGenerator instance.

        make_meme(self, img_path: str, text: str, author: str, width=500) -> str | None:
            Generate a meme using an image and caption text.

    """

    DEFAULT_FONT_SIZE = 24

    def __init__(self, output_dir: str, font: str):
        """
        Initialize a MemeGenerator instance.

        Args:
            output_dir (str): The directory where generated memes will be saved.
            font (str): The path to the font file to be used for captions.

        """
        self._output_dir = output_dir
        self._font_path = font
        os.makedirs(output_dir, exist_ok=True)

    def make_meme(self, img_path: str, text: str, author: str, width=500) -> str | None:
        """
        Generate a meme using an image and caption text.

        Args:
            img_path (str): The path to the image to be used for the meme.
            text (str): The caption text to be added to the meme.
            author (str): The author's name to be added to the meme.
            width (int): The desired width for the resulting meme image (default is 500).

        Returns:
            str | None: The path to the generated meme image if successful, or None on failure.

        """
        try:
            img = Image.open(img_path)
            img = _resize_image(img, width)

            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(self._font_path, size=self.DEFAULT_FONT_SIZE)

            text_x, text_y = _get_random_caption_position(img)
            caption = f"{text} - {author}"
            draw.text((text_x, text_y), caption, font=font, fill="#f20f0f")

            result_path = os.path.join(self._output_dir, f'meme_{random.randint(1, 10000)}.jpg')
            img.save(result_path)

            return result_path
        except (FileNotFoundError, IOError) as file_error:
            print(f"Error occurred: {file_error}")
            return None


def _get_random_caption_position(img: Image.Image) -> tuple:
    """
    Get a random position for the caption text on the image.

    Args:
        img (Image.Image): The image to which the caption will be added.

    Returns:
        tuple: A tuple containing the x and y coordinates for the caption's position.

    """
    max_x = img.width - 150
    max_y = img.height - 30
    text_x = random.randint(10, max_x)
    text_y = random.randint(10, max_y)
    return text_x, text_y


def _resize_image(img: Image.Image, width: int) -> Image.Image:
    """
    Resize an image to the specified width while maintaining its aspect ratio.

    Args:
        img (Image.Image): The image to be resized.
        width (int): The desired width for the resized image.

    Returns:
        Image.Image: The resized image.

    """
    ratio = width / float(img.width)
    height = int(ratio * float(img.height))
    return img.resize((width, height), Image.NEAREST)
