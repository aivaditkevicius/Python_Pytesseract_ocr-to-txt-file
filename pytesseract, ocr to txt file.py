import pytesseract
import requests
from bs4 import BeautifulSoup
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
tekstas=pytesseract.image_to_string(r'C:\Users\alma\Desktop\testas.png')
print(tekstas)
f=open("testas222.txt","w")
f.write(tekstas)
print("success")
f.close()
