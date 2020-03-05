import pytesseract
from PIL import Image
import cv2
img = cv2.imread('1.png',cv2.IMREAD_COLOR)
gray = cv2.resize(img, (620,480))
gray = cv2.bilateralFilter(gray, 11, 17, 17)

original = pytesseract.image_to_string(gray, config='')
print(original)
