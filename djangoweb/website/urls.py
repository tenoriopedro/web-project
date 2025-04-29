from django.urls import path
from website.views import home, contacts, who_we_are

app_name = 'website'

urlpatterns = [
    path('', home, name='home'),
    path('contatos/', contacts, name='contacts'),
    path('quem-somos/', who_we_are, name='who_we_are'),
]
