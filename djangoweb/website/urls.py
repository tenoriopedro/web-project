from django.urls import path
from website import views

app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('contatos/', views.contacts, name='contacts'),
    path('contatos/sucesso/', views.success_form, name='success_form'),
    path('quem-somos/', views.who_we_are, name='who_we_are'),
]
