from django.contrib import admin
from website.models import (FeaturedProducts, WhyGazil,
                            Contacts, SocialAprovation)


@admin.register(FeaturedProducts)
class FeaturedProductsAdmin(admin.ModelAdmin):
    list_display = 'id', 'title',
    ordering = '-id',


@admin.register(WhyGazil)
class WhyGazilAdmin(admin.ModelAdmin):
    list_display = 'id', 'title',
    ordering = 'id',


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'email', 'created_at',
    search_fields = 'first_name', 'last_name', 'email',
    readonly_fields = (
        'first_name', 'last_name', 'email',
        'message', 'created_at',
    )
    ordering = '-created_at',


@admin.register(SocialAprovation)
class SocialAprovationAdmin(admin.ModelAdmin):
    list_display = 'id', 'image', 'created_at',
