from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.urls import reverse
from site_setup.models import SubMenuLink
from utils.random_letters import slugify_new
from utils.model_validator import validate_png
from utils.image_upload_path import product_image_upload_path
from utils.save_check import check_product_image


class Products(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    name = models.CharField(max_length=255, verbose_name='Nome')
    product_type = models.ForeignKey(
        "ProductsSetup",
        on_delete=models.CASCADE,
        verbose_name='Tipo de Produto',
    )
    short_description = models.TextField(
        max_length=255, verbose_name='Descrição Curta'
    )
    long_description = models.TextField(verbose_name='Descrição Longa')
    image = models.ImageField(
        upload_to=product_image_upload_path,
        blank=False,
        null=False,
        verbose_name='Imagem do produto',
    )
    slug_product = models.SlugField(
        unique=True,
        blank=True,
        null=True,
        verbose_name='Slug do Produto'
    )

    def save(self, *args, **kwargs):
        if not self.slug_product:
            self.slug_product = slugify_new(self.name)

        current_image_name = str(self.image.name)
        super().save(*args, **kwargs)

        check_product_image(self.image, current_image_name)

    def get_absolute_url(self):
        return reverse(
            "products:product-detail",
            kwargs={
                "slug_category": self.product_type.slug_category,
                "slug_product": self.slug_product,
            }
        )

    def __str__(self):
        return f"{self.name}"


class ProductsSetup(models.Model):
    class Meta:
        ordering = ['product_type']
        verbose_name = 'Produto(Setup)'
        verbose_name_plural = 'Produtos(Setup)'

    product_type = models.ForeignKey(
        SubMenuLink,
        on_delete=models.CASCADE,
        verbose_name='Tipo de Produto',
    )
    image = models.ImageField(
        upload_to=product_image_upload_path,
        validators=[validate_png],
        blank=False,
        null=False,
        verbose_name='Imagem do produto',
    )
    slug_category = models.SlugField(
        unique=True,
        blank=True,
        null=True,
        verbose_name='Slug da Categoria'
    )

    def save(self, *args, **kwargs):
        if not self.slug_category:
            self.slug_category = slugify(self.product_type.text)

        super().save(*args, **kwargs)

    def clean(self):
        if ProductsSetup.objects.filter(
            product_type=self.product_type).exclude(
                pk=self.pk).exists():

            raise ValidationError(
                f"Já existe um produto do tipo '{self.product_type}'."
                "Apenas um é permitido."
            )

    def get_absolute_url(self):
        return reverse(
            "products:product-list",
            args=[self.slug_category],
        )

    def __str__(self):
        return f"{self.product_type.text}"


class SobMedidaProject(models.Model):

    title = models.CharField(max_length=100, verbose_name='Título')
    image_sob_medida = models.ImageField(
        upload_to='portfolio_sob_medida/%Y/%m',
        verbose_name='Imagem'
    )
    description = models.TextField(blank=True, verbose_name='Descrição')
    order = models.PositiveIntegerField(default=0, verbose_name='Ordem')

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Item do Portfólio"
        verbose_name_plural = "Itens do Portfólio(Sob Medida)"

    def __str__(self):
        return self.title
