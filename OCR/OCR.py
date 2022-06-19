#importing the open source OCR library
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#importing cv library for handling images
import cv2
img = cv2.imread("resources//Text.png")
cv2.imshow("Sample Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

text = pytesseract.image_to_string(img)
print(text)
