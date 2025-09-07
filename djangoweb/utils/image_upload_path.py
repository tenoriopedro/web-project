import os
from django.utils.text import slugify
from datetime import datetime


def product_image_upload_path(instance, filename):

    base_folder = 'image_products_setup' if instance._meta.model_name == 'productssetup' else 'image_products'
    if instance._meta.model_name == 'productssetup':
        product_type = slugify(
            instance.product_type.text 
            if instance.product_type else "sem-tipo"
        )
    else:  # Products
        product_type = slugify(
            instance.product_type.slug_category 
            if instance.product_type else "sem-categoria"
        )

    return os.path.join(
        base_folder,
        product_type,
        datetime.now().strftime('%Y'),
        datetime.now().strftime('%m'),
        filename
    )