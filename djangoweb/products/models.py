from django.db import models
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.urls import reverse
from site_setup.models import SubMenuLink
from utils.images import resize_image_product
from utils.random_letters import slugify_new
from utils.image_upload_path import product_image_upload_path



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
    short_description = models.TextField(max_length=255, verbose_name='Descrição Curta', default="Lorem ipsum dolor sit amet consectetur adipisicing elit. Harum, fuga. Neque expedita nihil sint.")
    long_description = models.TextField(verbose_name='Descrição Longa', default="Lorem ipsum dolor sit amet consectetur adipisicing elit. Harum, fuga. Neque expedita nihil sint. Harum saepe atque facilis velit sunt, nihil ea reiciendis nulla et facere. Fugit tempore repellat maiores!Lorem ipsum dolor sit amet consectetur adipisicing elit. Harum, fuga. Neque expedita nihil sint. Harum saepe atque facilis velit sunt, nihil ea reiciendis nulla et facere. Fugit tempore repellat maiores!")
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

        super().save(*args, **kwargs)

        max_image_size = 800
        if self.image:
            resize_image_product(self.image, max_image_size)

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

        max_image_size = 600
        if self.image:
            resize_image_product(self.image, max_image_size)

    def clean(self):
        if ProductsSetup.objects.filter(
            product_type=self.product_type).exclude(
                pk=self.pk
            ).exists():

            raise ValidationError(f"Já existe um produto do tipo '{self.product_type}'. Apenas um é permitido.")

    def __str__(self):
        return f"{self.product_type.text}"
    

