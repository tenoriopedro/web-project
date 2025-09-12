from django.db import models


class FeaturedProducts(models.Model):

    class Meta:
        verbose_name = "Produto Destacado"
        verbose_name_plural = "Produtos Destacados"

    title = models.CharField(max_length=300, blank=True, verbose_name='Título')
    description = models.CharField(
        max_length=1000, default='', blank=True, verbose_name='Descrição'
    )
    button_name = models.CharField(
        max_length=50, blank=True, verbose_name='Button Name'
    )
    button_link = models.CharField(
        max_length=100, blank=True, verbose_name='Button Link'
    )
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
    description = models.TextField(
        default='', blank=True, verbose_name='Descrição'
    )
    icon = models.CharField(max_length=10, default='', verbose_name='Ícone')

    def __str__(self):
        return self.title


class Contacts(models.Model):

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


class SocialAprovation(models.Model):

    class Meta:
        verbose_name = "Aprovação Social"
        verbose_name_plural = "Aprovações Sociais"
        ordering = ['-created_at']

    image = models.ImageField(
        upload_to='assets/social_aprovation/%Y/%m',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Client Image {self.id}"
