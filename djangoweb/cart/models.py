from django.db import models
from products.models import Products


class BudgetRequest(models.Model):

    class Meta:
        verbose_name = 'Pedido de Orçamento'
        verbose_name_plural = 'Pedidos de Orçamentos'

    name = models.CharField(max_length=100, verbose_name="Nome")
    phone = models.CharField(max_length=20, verbose_name="Telefone")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(blank=True, null=True, verbose_name="Mensagem")
    products = models.ManyToManyField(Products, related_name="budget_requests")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"""
Orçamento de 
{self.name} ({self.email}) - 
{self.created_at:%Y-%m-%d}
"""

