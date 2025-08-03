from django.urls import path
from products.views import index, BancadaListView,BancadaDetailView

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('bancadas/', BancadaListView.as_view(), name='bancadas-list'),
    path('bancadas/<slug:slug>', BancadaDetailView.as_view(), name='bancada-detail'),


]