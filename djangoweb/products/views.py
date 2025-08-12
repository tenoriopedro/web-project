from django.views.generic import TemplateView, ListView, DetailView
from .models import Products
from site_setup.models import SiteSetup


class ProductsIndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        categories = Products.objects.values('product_type__text').distinct()
        context = {
            'categories': [
                categorie['product_type__text'] 
                for categorie in categories
            ]
        }

        return context


class ProductsListView(ListView):
    model = Products
    template_name = 'products/list_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        product_type = self.kwargs['product_type']
        return Products.objects.filter(
            product_type__text=product_type
        )


class ProductDetailView(DetailView):
    model = Products
    template_name = 'products/detail_product.html'
    context_object_name = 'product'
