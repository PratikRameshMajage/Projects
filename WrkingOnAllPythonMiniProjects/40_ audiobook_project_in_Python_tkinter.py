import pyttsx3
import PyPDF2

# Open the PDF file and create a PDF reader object
pdf_file = open('example.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Loop through the pages of the PDF file and read each page
for page in pdf_reader.pages:
    text = page.text
    engine.say(text)

# Run the text-to-speech engine
engine.runAndWait()

# Close the PDF file
pdf_file.close()
