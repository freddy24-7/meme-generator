```markdown
# Meme Generator

A simple Python application for generating memes by adding captions to images.

## Overview

This project provides a command-line tool for generating memes by adding text captions to existing images. It supports various image formats and allows customization of the meme's caption, author, and output directory.

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/freddy24-7/meme-generator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd meme-generator
   ```

## Usage

### Generate a Random Meme

You can generate a random meme without specifying an image or caption by starting the Flask server:

```bash
python app.py
```

By default, the application will use random images and quotes from predefined data sources.
Once the application is running, you can add your own images and captions.

## Sub-Modules

### `QuoteEngine`

The `QuoteEngine` module is responsible for ingesting quotes from various file formats, including CSV, DOCX, PDF, and plain text files.

- `CSVIngestor`: Ingests quotes from CSV files.
- `DocxIngestor`: Ingests quotes from DOCX files.
- `PDFIngestor`: Ingests quotes from PDF files.
- `TextIngestor`: Ingests quotes from plain text files.

### `MemeGenerator`

The `MemeGenerator` module handles the generation of memes. It resizes images, adds captions with custom fonts and colors, and saves the resulting memes to an output directory.

## Dependencies
blinker==1.6.3
certifi==2023.7.22
charset-normalizer==3.3.0
click==8.1.7
Flask==3.0.0
idna==3.4
itsdangerous==2.1.2
Jinja2==3.1.2
lxml==4.9.3
MarkupSafe==2.1.3
numpy==1.26.0
pandas==2.1.1
Pillow==10.1.0
python-dateutil==2.8.2
python-docx==1.0.1
pytz==2023.3.post1
requests==2.31.0
six==1.16.0
typing_extensions==4.8.0
tzdata==2023.3
urllib3==2.0.6
Werkzeug==3.0.0


