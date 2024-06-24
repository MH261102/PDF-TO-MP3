import pyttsx3
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog

def select_pdf_file():
    root = tk.Tk()
    root.withdraw() # Hides the main window
    file_path = filedialog.askopenfilename(
        title = "Select PDF File",
        filetypes=(("PDF files", "*.pdf"), ("All files", "*.*"))
    )
    return file_path

def main():
    pdf_file_path = select_pdf_file()
    if not pdf_file_path:
        print("No path was selected.")
        return
    

    pdf_reader = PdfReader(open(pdf_file_path, 'rb'))

    speaker = pyttsx3.init()

    # Extract text and read aloud
    clean_text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        clean_text += text.strip().replace('\n', ' ') + ' '

    # Save the extracted text to an mp3 file
    speaker.save_to_file(clean_text, 'story.mp3')
    speaker.runAndWait()

    # Stop the speaker
    speaker.stop()

if __name__ == "__main__":
    main()

