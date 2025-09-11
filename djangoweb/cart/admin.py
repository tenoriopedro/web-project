from django.apps import apps
from django.contrib import admin
from cart.models import BudgetRequest


app_config = apps.get_app_config('cart')
app_config.verbose_name = "Orçamentos"


@admin.register(BudgetRequest)
class BudgetRequestAdmin(admin.ModelAdmin):
    list_display = 'name', 'phone', 'email', 'created_at',
    search_fields = 'first_name', 'email',
    readonly_fields = (
        'name', 'phone', 'email', 'message', 'created_at',
        'get_products',
    )
    ordering = '-created_at',
    exclude = 'products',

    def get_products(self, obj):
        return ", ".join([
            p.name for p in obj.products.all()
        ])

    get_products.short_description = "Produtos"
