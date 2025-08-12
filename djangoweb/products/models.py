from django.db import models
from utils.images import resize_image
from utils.random_letters import slugify_new
from site_setup.models import SubMenuLink



class Products(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    name = models.CharField(max_length=255, verbose_name='Nome')
    short_description = models.TextField(max_length=255, verbose_name='Descrição Curta')
    long_description = models.TextField(verbose_name='Descrição Longa')
    image = models.ImageField(
        upload_to='image_products/%Y/%m/',
        blank=False,
        null=False,
        verbose_name='Imagem do produto',
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
    )
    product_type = models.ForeignKey(
        SubMenuLink, 
        on_delete=models.CASCADE,
        verbose_name='Tipo de Produto',
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)

        super().save(*args, **kwargs)

        max_image_size = 800
        if self.image:
            resize_image(self.image, max_image_size)

    def __str__(self):
        return f" {self.name} ({self.product_type.text})"
    