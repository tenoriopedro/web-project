from utils.images import resize_image, resize_image_product


def _check_image(image, current_image_name, size):

    image_changed = False

    if image:
        image_changed = current_image_name != image.name

    if image_changed:

        resize_func = resize_image_product if size >= 600 else resize_image
        new_image = resize_func(image, size)

        return new_image

    return


def check_favicon(image, current_image_name):
    return _check_image(
        image, current_image_name, size=64
    )


def check_product_image(image, current_image_name):
    return _check_image(
        image, current_image_name, size=800
    )
