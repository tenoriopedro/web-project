from pathlib import Path
from django.conf import settings
from PIL import Image


def resize_image(image_django, new_width=800, optimize=True, quality=70):

    image_path = Path(settings.MEDIA_ROOT / image_django.name).resolve()
    image_pillow = Image.open(image_path)
    original_width, original_height = image_pillow.size

    if original_width <= new_width:
        image_pillow.close()
        return image_pillow

    new_height = round(new_width * original_height / original_width)

    new_image = image_pillow.resize(
        (new_width, new_height),
        Image.LANCZOS
    )
    new_image.save(
        image_path,
        optimize=optimize,
        quality=quality,
    )

    return new_image


def resize_image_product(image_django, size=800, optimize=True, quality=90):
    image_path = Path(settings.MEDIA_ROOT / image_django.name).resolve()

    image_pillow = Image.open(image_path).convert("RGB")
    original_width, original_height = image_pillow.size

    if original_width <= size and original_height <= size:
        image_pillow.close()
        return image_pillow

    image_pillow.thumbnail((size, size), Image.LANCZOS)

    new_image = Image.new("RGB", (size, size), (255, 255, 255))

    # Calculates the coordinates of the central crop
    left = (size - image_pillow.width) // 2
    top = (size - image_pillow.height) // 2

    new_image.paste(image_pillow, (left, top))

    # Saves replacing the original image
    new_image.save(
        image_path,
        optimize=optimize,
        quality=quality,
    )

    return new_image
