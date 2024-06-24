# PDF to MP3 Converter

This project is a Python application that converts text from a PDF file to speech and saves it as an MP3 file. It utilizes the `PyPDF2` library to read the PDF file and `pyttsx3` to convert the extracted text to speech.

## Features

- Select a PDF file using a file dialog
- Extract text from the PDF file
- Convert extracted text to speech
- Save the speech as an MP3 file

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/pdf-to-speech-converter.git
    cd pdf-to-speech-converter
    ```

2. Install the required libraries using `requirements.txt`:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script:
    ```sh
    python main.py
    ```

2. A file dialog will appear. Select the PDF file you want to convert.

3. The application will extract the text from the PDF, convert it to speech, and save it as `story.mp3` in the current directory.

## Code Overview

- `select_pdf_file()`: Opens a file dialog to select a PDF file.
- `main()`: The main function that orchestrates the workflow:
  - Calls `select_pdf_file()` to get the path of the PDF file.
  - Reads the PDF file using `PyPDF2`.
  - Extracts text from each page.
  - Converts the extracted text to speech using `pyttsx3`.
  - Saves the speech as an MP3 file.

## Contribution

Contributions are welcome! Please open an issue or submit a pull request for any changes or additions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
