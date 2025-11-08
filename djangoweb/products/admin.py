from django.contrib import admin
from django.apps import apps
from .models import (
    Products, ProductsSetup, SobMedidaRequest, SobMedidaPortfolio)


app_config = apps.get_app_config('products')
app_config.verbose_name = "Produtos"


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = 'name', 'product_type', 'slug_product',
    list_filter = 'product_type',
    search_fields = 'name', 'product_type'

    fieldsets = (
        (None, {
            'fields': ('name', 'product_type', 'slug_product')
        }),
        ('Descrição', {
            'fields': ('short_description', 'long_description')
        }),
        ('Imagem', {
            'fields': ('image',)
        }),
    )


@admin.register(ProductsSetup)
class ProductsSetupAdmin(admin.ModelAdmin):
    list_display = 'product_type', 'slug_category',
    ordering = 'product_type',


@admin.register(SobMedidaPortfolio)
class SobMedidaProjectAdmin(admin.ModelAdmin):

    list_display = 'title', 'order',
    list_editable = 'order',
    search_fields = 'title', 'description',
    fields = 'title', 'description', 'image_sob_medida', 'order',


@admin.register(SobMedidaRequest)
class SobMedidaRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'has_attachment')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'phone', 'project_description')

    readonly_fields = [f.name for f in SobMedidaRequest._meta.fields]

    def has_attachment(self, obj):
        return bool(obj.attachment)

    has_attachment.boolean = True
    has_attachment.short_description = "Anexo?"

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
