from django.contrib import admin
from cart.models import BudgetRequest

@admin.register(BudgetRequest)
class BudgetRequestAdmin(admin.ModelAdmin):
    list_display = 'name', 'phone', 'email', 'created_at',
    search_fields = 'first_name', 'email',
    readonly_fields = 'name', 'phone', 'email','message', 'created_at',
    ordering = '-created_at',