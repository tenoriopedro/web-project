from django.views.generic import TemplateView, ListView, DetailView
from .models import Products, ProductsSetup
from django.shortcuts import get_object_or_404


class ProductsIndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        categories = ProductsSetup.objects.all()
        context = {
            'categories': categories
        }

        return context
        

class ProductsListView(ListView):
    model = Products
    template_name = 'products/list_products.html'
    context_object_name = 'products'
    paginate_by = 8


    def get_queryset(self):
        category_slug = self.kwargs['slug_category']
        category = ProductsSetup.objects.get(slug_category=category_slug)

        queryset = Products.objects.filter(
            product_type=category.product_type
        )

        order = self.request.GET.get('order', 'name')
        if order in ['name', '-name', 'id', '-id']:
            queryset = queryset.order_by(order)

        return queryset
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        slug_category = self.kwargs.get('slug_category')

        context['current_order'] = self.request.GET.get('order', 'name')
        context['slug_category'] = slug_category

        return context
        


class ProductDetailView(DetailView):
    model = Products
    template_name = 'products/detail_product.html'
    context_object_name = 'products'
    slug_url_kwarg = "slug_product"


    def get_object(self):

        slug_category = self.kwargs.get("slug_category")
        slug_product = self.kwargs.get("slug_product")

        return get_object_or_404(
            Products,
            slug_product=slug_product
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object

        related_products = (
            Products.objects.filter(
                product_type=product.product_type
            ).exclude(id=product.id)[:4]
        )
        context["related_products"] = related_products
        context["slug_category"] = self.kwargs.get('slug_category')
        context["product"] = product
        
        return context
    