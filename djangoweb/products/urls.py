from django.urls import path
from products.views import ProductsIndexView, ProductsListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('', ProductsIndexView.as_view(), name='index'),
    path(
        '<slug:slug_category>/', 
        ProductsListView.as_view(), 
        name='product-list'
    ),
    
    path(
        '<slug:slug_category>/<slug:slug_product>/',
        ProductDetailView.as_view(),
        name='product-detail'
    ),
]