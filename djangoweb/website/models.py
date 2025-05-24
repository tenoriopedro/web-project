from django.db import models 


class FeaturedProducts(models.Model):

    class Meta:
        verbose_name = "Produto Destacado"
        verbose_name_plural = "Produtos Destacados"

    title = models.CharField(max_length=300, blank=True, verbose_name='Título')
    description = models.CharField(max_length=1000, default='', blank=True, verbose_name='Descrição')
    button_name = models.CharField(max_length=50, blank=True, verbose_name='Button Name')
    button_link = models.CharField(max_length=100, blank=True, verbose_name='Button Link')
    image = models.ImageField(
        upload_to='assets/featured_products/%Y/%m', 
        blank=True, default='', verbose_name='Imagem'
    )

    def __str__(self):
        return self.title

class WhyGazil(models.Model):

    class Meta:
        verbose_name = "Por que Gazil"
        verbose_name_plural = "Por que Gazil"

    title = models.CharField(max_length=50, default='', verbose_name='Título')
    description = models.TextField(default='', blank=True, verbose_name='Descrição')
    icon = models.CharField(max_length=10, default='', verbose_name='Ícone')

    def __str__(self):
        return self.title
    