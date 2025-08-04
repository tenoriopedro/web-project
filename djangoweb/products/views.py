from django.views.generic import TemplateView, ListView, DetailView
from .models import Products


class ProductsIndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        categories = Products.objects.values('product_type').distinct()
        context = {'categories': categories}

        return context


class ProductsListView(ListView):
    model = Products
    template_name = 'products/list_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Products.objects.filter(product_type=self.kwargs['product_type'])


class ProductDetailView(DetailView):
    model = Products
    template_name = 'products/detail_product.html'
    context_object_name = 'product'