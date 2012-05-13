import Image

def image_resize(image, size):
    if not isinstance(image, Image):
        raise TypeError(str(image) + ' is not instance of Image(PIL)')

    newWidth = size[0]
    newHeight = size[1]

    oldWidth = image.size[0]
    oldHeight = image.size[1]

    width = newWidth
    height = width * oldHeight / oldWidth

    if height > newHeight:
        height = newHeight
        width = height * old_width / old_height

    return image.resize((width, height), Image.ANTIALIAS)