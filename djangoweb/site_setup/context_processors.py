from site_setup.models import SiteSetup
from products.models import ProductsSetup

def site_setup(request):
    data = SiteSetup.objects.order_by('-id').first()
    product_path = ProductsSetup.objects.all()
    
    return {
        'site_setup': data,
        'products_setup_list': product_path,
    }