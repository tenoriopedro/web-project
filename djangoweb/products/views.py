from django.views.generic import TemplateView, ListView, DetailView
from .models import Products, ProductsSetup
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.urls import reverse
from utils.mixins import BreadcrumbsMixin


class ProductsIndexView(BreadcrumbsMixin, TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context["categories"] = ProductsSetup.objects.all()
        return context
        
    def get_breadcrumbs(self):
        return [
            {"name": "Home", "url": reverse("website:home")},
            {"name": "Produtos", "url": reverse("products:index")},
        ]

class ProductsListView(BreadcrumbsMixin, ListView):
    model = Products
    template_name = 'products/list_products.html'
    context_object_name = 'products'
    paginate_by = 8


    def get_queryset(self):
        category_slug = self.kwargs['slug_category']
        self.category = ProductsSetup.objects.get(slug_category=category_slug)

        queryset = Products.objects.filter(
            product_type=self.category
        )

        order = self.request.GET.get('order', 'name')
        if order in ['name', '-name', 'id', '-id']:
            queryset = queryset.order_by(order)

        return queryset
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['current_order'] = self.request.GET.get('order', 'name')
        context['slug_category'] = self.category.slug_category
        context['name_category'] = self.category
        context["is_search"] = False

        return context
    
    def get_breadcrumbs(self):
        return [
            {"name": "Home", "url": reverse("website:home")},
            {"name": "Produtos", "url": reverse("products:index")},
            {"name": self.category.product_type.text, "url": self.category.get_absolute_url()},
        ]
        

class ProductDetailView(BreadcrumbsMixin, DetailView):
    model = Products
    template_name = 'products/detail_product.html'
    context_object_name = 'products'
    slug_url_kwarg = "slug_product"

    def get_object(self):

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
    
    def get_breadcrumbs(self):
        product = self.get_object()
        category = product.product_type
        return [
            {"name": "Home", "url": reverse("website:home")},
            {"name": "Produtos", "url": reverse("products:index")},
            {"name": category, "url": category.get_absolute_url()},
            {"name": product.name, "url": product.get_absolute_url()},
        ]
    

class ProductsSearchView(ListView):
    model = Products
    template_name = 'products/list_products.html'
    context_object_name = "products"
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        queryset = Products.objects.all().select_related("product_type")

        if query:

            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(short_description__icontains=query) |
                Q(product_type__slug_category__icontains=query)
            )

        return queryset
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q", "")
        context["q"] = query
        context["is_search"] = True
        context["breadcrumbs"] = [
            {"name": "Home", "url": reverse("website:home")},
            {"name": "Produtos", "url": reverse("products:index")},
            {"name": f"Pesquisa por '{query}'", "url": None},
        ]
        return context
    

def cart_view(request):
    return render(
        request,
        'products/cart.html'
    )