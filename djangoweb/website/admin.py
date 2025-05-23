from django.contrib import admin
from website.models import FeaturedProducts


@admin.register(FeaturedProducts)
class FeaturedProductsAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'description', 'button_name', 'button_link',
    ordering = '-id',