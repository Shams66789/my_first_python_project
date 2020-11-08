import PyPDF2
import pyttsx3

book = open('op.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
print(pages)
spe = pyttsx3.init()
page = pdfreader.getPage(2)
text = page.extractText()
spe.say(text)
spe.runAndWait()