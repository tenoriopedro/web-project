from django.urls import path
from products.views import (ProductsIndexView, ProductsListView,
                            ProductDetailView, ProductsSearchView,
                            CustomMadeView
                            )

app_name = 'products'

urlpatterns = [

    # Index Page
    path('', ProductsIndexView.as_view(), name='index'),

    # Sob Medida Page
    path('sob-medida/', CustomMadeView.as_view(), name='custom-made'),

    # Search Page
    path(
        "pesquisa/",
        ProductsSearchView.as_view(),
        name="products-search"
    ),

    # List Page
    path(
        '<slug:slug_category>/',
        ProductsListView.as_view(),
        name='product-list'
    ),

    # Detail Page
    path(
        '<slug:slug_category>/<slug:slug_product>/',
        ProductDetailView.as_view(),
        name='product-detail'
    ),
]
