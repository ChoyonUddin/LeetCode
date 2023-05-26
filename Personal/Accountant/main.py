from tkinter import PAGES
import webbrowser
import PyPDF2
from PyPDF2 import PdfReader
visa = "C:\Programming\Python\Personal\Accountant\Visa Statement-2508 2022-09-15.pdf"
#ebbrowser.open_new_tab(visa)




#print(PdfReader(visa).pages[0].extract_text())
print(PdfReader(visa).pages)