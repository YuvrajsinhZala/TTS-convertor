from pytesseract import image_to_string
import pytesseract
from PIL import Image
img=Image.open('2.png')
a=pytesseract.image_to_string(img)
print(a)

