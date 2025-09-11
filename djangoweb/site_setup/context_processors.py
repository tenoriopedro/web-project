from site_setup.models import SiteSetup
from products.models import ProductsSetup


def site_setup(request):
    data = SiteSetup.objects.order_by('-id').first()
    product_path = ProductsSetup.objects.all()
    cart = request.session.get("cart", [])

    return {
        'site_setup': data,
        'products_setup_list': product_path,
        "cart_item_count": len(cart)
    }
