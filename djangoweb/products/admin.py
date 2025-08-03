from django.contrib import admin
from django.apps import apps
from .models import Bancadas


app_config = apps.get_app_config('products')
app_config.verbose_name = "Produtos"


@admin.register(Bancadas)
class AdminBancadas(admin.ModelAdmin):
    list_display = 'name',
