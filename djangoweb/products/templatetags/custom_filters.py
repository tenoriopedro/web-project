from django import template
from urllib.parse import quote

register = template.Library()


@register.filter
def build_absolute_url(request, relative_url):
    return request.build_absolute_uri(relative_url)

@register.filter
def whatsapp_product_message(product, request):
    message = f"""
Olá, gostaria de saber o preço do produto: {product.name}
Descrição: {product.short_description}
Link: {request.build_absolute_uri(product.slug_product)}
"""
    return quote(message)