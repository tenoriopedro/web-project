from django.db import models
from utils.images import resize_image
from utils.random_letters import slugify_new
from site_setup.models import SubMenuLink
from django.core.exceptions import ValidationError
from utils.image_upload_path import product_image_upload_path



class Products(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    name = models.CharField(max_length=255, verbose_name='Nome')
    product_type = models.ForeignKey(
        SubMenuLink, 
        on_delete=models.CASCADE,
        verbose_name='Tipo de Produto',
    )
    short_description = models.TextField(max_length=255, verbose_name='Descrição Curta')
    long_description = models.TextField(verbose_name='Descrição Longa')
    image = models.ImageField(
        upload_to=product_image_upload_path,
        blank=False,
        null=False,
        verbose_name='Imagem do produto',
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)

        super().save(*args, **kwargs)

        max_image_size = 800
        if self.image:
            resize_image(self.image, max_image_size)

    def __str__(self):
        return f"{self.name}"
    

class ProductsSetup(models.Model):
    class Meta:
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

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        max_image_size = 800
        if self.image:
            resize_image(self.image, max_image_size)

    def clean(self):
        if ProductsSetup.objects.filter(
            product_type=self.product_type).exclude(
                pk=self.pk
            ).exists():

            raise ValidationError(f"Já existe um produto do tipo '{self.product_type}'. Apenas um é permitido.")

    def __str__(self):
        return f"{self.product_type.text}"
    

