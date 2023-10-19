"""
Meme Generation Script.

This script allows you to generate memes by combining random or user-defined images with quotes.

Usage:
1. Run the script using Python with optional command-line arguments:
   - `--path` (optional): Path to a specific image file.
   - `--body` (optional): Quote body to add to the image.
   - `--author` (optional): Quote author to add to the image.

2. The script will generate a meme using the provided image, quote body, and author (if provided), or it will use random images and quotes from predefined sources.

3. The generated meme will be saved in the './tmp' directory with a random filename.

Example:
   To generate a meme with a specific image and custom text:
   ```bash
   python script.py --path path_to_image.jpg --body "Custom text" --author "Custom author"
   Requirements:

    QuoteEngine (Custom module for ingesting quotes)
    MemeGenerator (Custom module for generating memes)
"""

import os
import random
import argparse
from QuoteEngine.Ingestor import Ingestor
from MemeGenerator.MemeGenerator import MemeGenerator
from QuoteEngine import QuoteModel


def get_random_image(images_directory):
    """
    Get a random image path from the specified directory.

    :param images_directory: The directory containing image files.
    :return: Path to a random image file.
    """
    image_files = [os.path.join(images_directory, name) for name in os.listdir(images_directory)]
    return random.choice(image_files)


def get_random_quote(quote_files):
    """
    Get a random quote from the specified list of quote files.

    :param quote_files: List of quote file paths.
    :return: A random quote.
    """
    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    return random.choice(quotes)


def generate_meme(options):
    """
    Generate a meme based on the specified options.

    :param options: A dictionary containing options for image, body, and author.
    :return: Path to the created meme image, or None if an error occurs.
    """
    img = options.get('image', None)
    body = options.get('body', None)
    author = options.get('author', None)

    if img is None:
        images_directory = "./_data/photos/dog/"
        img = get_random_image(images_directory)

    if body is None:
        quote_files = [
            './_data/DogQuotes/DogQuotesTXT.txt',
            './_data/DogQuotes/DogQuotesDOCX.docx',
            './_data/DogQuotes/DogQuotesPDF.pdf',
            './_data/DogQuotes/DogQuotesCSV.csv'
        ]
        quote = get_random_quote(quote_files)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel.QuoteModel(body, author)

    font_path = "font/Arial.ttf"
    meme = MemeGenerator('./tmp', font_path)
    generate_path = meme.make_meme(img, quote.body, quote.author)
    return generate_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a meme.")
    parser.add_argument("--image", type=str, help="Path to an image file")
    parser.add_argument("--body", type=str, help="Quote body to add to the image")
    parser.add_argument("--author", type=str, help="Quote author to add to the image")
    args = parser.parse_args()

    options = {
        'image': args.image,
        'body': args.body,
        'author': args.author
    }

    generated_path = generate_meme(options)

    if generated_path:
        print(f"Meme generated and saved to: {generated_path}")
    else:
        print("Meme generation failed.")
