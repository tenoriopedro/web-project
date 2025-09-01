from django.urls import path
from cart.views import CartView, AddToCartView


app_name = "cart"

urlpatterns = [
    # Cart Page
    path("", CartView.as_view(), name="cart"),
    path(
        "adicionar/<slug:slug_product>/",
        AddToCartView.as_view(), 
        name="cart_add",
    ),
]
