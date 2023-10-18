"""
Meme Generator Flask Application.

This Flask application generates memes by adding captions to images. It allows users to create memes using their own images and captions or generate random memes from predefined quotes and images.

Requirements:
- Flask
- Pillow (PIL Fork)
- QuoteEngine (Custom module for ingesting quotes)
- MemeGenerator (Custom module for generating memes)

Usage:
1. Run the application using Python:

   ```bash
   python app.py
Access the web application at http://localhost:5000/ in your web browser.

Follow the instructions on the web page to create custom memes or generate random memes.

"""

import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine.Ingestor import Ingestor
from MemeGenerator.MemeGenerator import MemeGenerator

app = Flask(__name__)

FONT_PATH = "font/Arial.ttf"
OUTPUT_DIR = "./static"
QUOTE_FILES = [
    './_data/DogQuotes/DogQuotesDOCX.docx',
    './_data/DogQuotes/DogQuotesPDF.pdf',
    './_data/DogQuotes/DogQuotesCSV.csv',
    './_data/DogQuotes/DogQuotesTXT.txt',
]
IMAGES_PATH = "./_data/photos/dog/"

meme = MemeGenerator(OUTPUT_DIR, FONT_PATH)


def setup():
    """Load all resources."""
    quotes_array = []

    for file in QUOTE_FILES:
        quotes_array.extend(Ingestor.parse(file))

    images = []

    for filename in os.listdir(IMAGES_PATH):
        image_path = os.path.join(IMAGES_PATH, filename)
        if os.path.isfile(image_path):
            images.append(image_path)

    return quotes_array, images


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template("meme_form.html")


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user-defined meme."""
    image_url = request.form['image_url']
    response = requests.get(image_url)

    if response.status_code != 200:
        abort(400, "Failed to fetch the image from the provided URL")

    temp_image_path = './temp_image.jpg'

    try:
        with open(temp_image_path, 'wb') as temp_image_file:
            temp_image_file.write(response.content)

        body = request.form['body']
        author = request.form['author']
        path = meme.make_meme(temp_image_path, body, author)

        return render_template('meme.html', path=path)
    except Exception as e:
        print(f"Error: {e}")
        abort(500, "An error occurred while processing the image")

    finally:
        if os.path.exists(temp_image_path):
            os.remove(temp_image_path)


if __name__ == "__main__":
    app.run()
