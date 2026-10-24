import PyPDF2
import pyttsx3


def convert_pdf_to_audio(pdf_file_path, output_audio_file):
    # Open the PDF file
    with open(pdf_file_path, "rb") as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Initialize the text variable to store extracted text
        full_text = ""

        # Extract text from each page of the PDF
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            full_text += page.extract_text()

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty("rate", 150)  # Speed of speech

    # Convert the extracted text to speech
    engine.save_to_file(full_text, output_audio_file)

    # Wait for the speech to finish
    engine.runAndWait()


# Example usage
pdf_file_path = "/Users/shamilabdullah/Downloads/Black Hat Python, 2nd Edition by Justin Seitz  Tim Arnold [Justin Seitz].pdf"
output_audio_file = "Teachings_audio.mp3"

convert_pdf_to_audio(pdf_file_path, output_audio_file)
