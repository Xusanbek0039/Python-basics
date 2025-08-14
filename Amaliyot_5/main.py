from rembg import remove
from PIL import Image
import os
import subprocess  # Windowsda rasmni ochish uchun

# Rasm nomi (shu papkada joylashgan bo'lishi kerak)
input_image_path = 'image.jpg'  # bu yerda o'zingizning rasm nomingizni yozing
output_image_path = 'rasm_nofon.png'

# Rasmni ochish va orqa fonni olib tashlash
with open(input_image_path, 'rb') as input_file:
    input_data = input_file.read()
    output_data = remove(input_data)

# Natijaviy rasmni saqlash
with open(output_image_path, 'wb') as output_file:
    output_file.write(output_data)

# Rasmni ochish (platformaga qarab)
def open_image(image_path):
    try:
        if os.name == 'nt':  # Windows
            os.startfile(image_path)
        elif os.name == 'posix':  # macOS yoki Linux
            subprocess.run(['open' if sys.platform == 'darwin' else 'xdg-open', image_path])
    except Exception as e:
        print(f"Rasmni ochishda xatolik: {e}")

# Natijani ochish
open_image(output_image_path)
