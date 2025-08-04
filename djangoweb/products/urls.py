from django.urls import path
from products.views import ProductsIndexView, ProductsListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('', ProductsIndexView.as_view(), name='index'),
    path(
        '<str:product_type>/', 
        ProductsListView.as_view(), 
        name='product-list'
    ),
    
    path(
        '<str:product_type>/<slug:slug>/',
        ProductDetailView.as_view(),
        name='product-detail'
    ),


]