import pytesseract

from PIL import Image

image=Image.open('/home/hello/2.png')
code=pytesseract.image_to_string(image,lang="chi_sim")
print(code)