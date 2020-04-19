# Image to text

import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


img = cv2.imread("power.png")
cv2.imshow('image', img)
cv2.waitKey(0)
text = pytesseract.image_to_string(img)
print(text)