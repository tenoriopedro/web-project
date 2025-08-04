from django.contrib import admin
from django.apps import apps
from .models import Products


app_config = apps.get_app_config('products')
app_config.verbose_name = "Produtos"


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = 'name', 'product_type', 'slug',
    list_filter = 'product_type',
    search_fields = 'name', 'product_type'
    prepopulated_fields = {'slug': ('name',)}

    fieldsets = (
        (None, {
            'fields': ('name', 'product_type', 'slug')
        }),
        ('Descrição', {
            'fields': ('short_description', 'long_description')
        }),
        ('Imagem', {
            'fields': ('image',)
        }),
    )