'''This simple Python script allows you to extract metadata from a JPEG image using the Pillow library in Python. Pillow is a library that
provides numerous functions to alter, manipulate or otherwise interact with images in Python. The data extracted is called EXIF
(Exchangeable Image File Format), which gives information about when and how an image was created.'''



from PIL import Image
from PIL.ExifTags import TAGS

#Use Pillow to read the given image filepath
image = input("Provide image path:")
read_image = Image.open(image)

#Read EXIF data within image
exif_data = read_image.getexif()

#Print out each item within the EXIF data
for tag, data in exif_data.items():
    data_tag = TAGS.get(tag, tag)

    print(f"{data_tag}: {data}")
