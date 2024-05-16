from pdf2image import convert_from_path
import PIL.Image
PIL.Image.MAX_IMAGE_PIXELS = 100005000
pages = convert_from_path('./W7_Lec13_ilp2.pdf', 400)

for count, page in enumerate(pages):
    page.save(f'./runthrough/slides/out{count}.jpg', 'JPEG')