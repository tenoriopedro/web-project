from utils.images import resize_image

def check_favicon(favicon, current_favicon_name, favicon_changed):
    favicon_changed_def = favicon_changed

    if favicon:
        favicon_changed_def = current_favicon_name != favicon.name

    if favicon_changed_def:
        new_image = resize_image(favicon, 64)

        return new_image

    else:
        return
    