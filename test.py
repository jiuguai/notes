import exifread
from PIL import Image

file_path = r"C:\Users\zero\Desktop\1.jpg"

with open(file_path, 'rb') as f:
    info = exifread.process_file(f)

print(info)

img = Image.open(file_path)
info = img._getexif()

print(info)

