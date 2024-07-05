from pdf2image import convert_from_path
import PIL.Image
PIL.Image.MAX_IMAGE_PIXELS = 100005000
pages = convert_from_path('./long_scripts/W5_Lec9_memorycache.pdf', 48)

for count, page in enumerate(pages):
    page.save(f'./long_scripts/slides/out{count}.jpg', 'JPEG')