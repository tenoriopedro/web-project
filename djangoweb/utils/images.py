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


def resize_image_product(image_django, size=800, optimize=True, quality=70):
    image_path = Path(settings.MEDIA_ROOT / image_django.name).resolve()
    image_pillow = Image.open(image_path).convert("RGB")
    original_width, original_height = image_pillow.size

    if max(original_width, original_height) <= size:
        image_pillow.close()
        return image_pillow

    # Resize proportionally
    # To ensure that the smallest side >= size
    ratio = size / min(original_width, original_height)
    new_width = int(original_width * ratio)
    new_height = int(original_height * ratio)
    image_pillow = image_pillow.resize(
        (new_width, new_height), Image.LANCZOS
    )

    # Calculates the coordinates of the central crop
    left = (new_width - size) // 2
    top = (new_height - size) // 2
    right = left + size
    bottom = top + size

    new_image = image_pillow.crop((left, top, right, bottom))

    # Saves replacing the original image
    new_image.save(
        image_path,
        optimize=optimize,
        quality=quality,
    )

    return new_image
