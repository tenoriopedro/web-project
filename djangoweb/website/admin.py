from django.contrib import admin
from website.models import FeaturedProducts, WhyGazil


@admin.register(FeaturedProducts)
class FeaturedProductsAdmin(admin.ModelAdmin):
    list_display = 'id', 'title',
    ordering = '-id',


@admin.register(WhyGazil)
class WhyGazilAdmin(admin.ModelAdmin):
    list_display = 'id', 'title',
    ordering = 'id',