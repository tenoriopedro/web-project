from django.contrib import admin
from django.apps import apps
from django.utils.translation import gettext_lazy as _
from site_setup.models import (MenuLink, SiteSetup,
                               Banner, SubMenuLink, Contacts
                               )


admin.site.index_title = _("Painel Administrativo")
admin.site.site_header = _("Administração Gazil")
admin.site.site_title = _("Admin Gazil")

app_config = apps.get_app_config('site_setup')
app_config.verbose_name = "Configurações do Site"


class MenuLinkInline(admin.TabularInline):
    model = MenuLink
    extra = 1


class SubMenuLinkInline(admin.TabularInline):
    model = SubMenuLink
    extra = 1
    readonly_fields = 'url_or_path',


class BannerInline(admin.TabularInline):
    model = Banner
    extra = 1


class ContactsInline(admin.StackedInline):
    model = Contacts
    extra = 0


@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description',
    inlines = ContactsInline, MenuLinkInline, SubMenuLinkInline, BannerInline,

    def has_add_permission(self, request):
        return not SiteSetup.objects.exists()
