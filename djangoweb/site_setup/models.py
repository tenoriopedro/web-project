from django.db import models
from utils.model_validator import validate_png
from utils.save_check import check_favicon
from django.core.validators import RegexValidator
from django.utils.text import slugify


class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'

    text = models.CharField(max_length=50, verbose_name='Texto')
    url_or_path = models.CharField(max_length=248)
    site_setup = models.ForeignKey(
        'SiteSetup', on_delete=models.CASCADE,
        blank=True, null=True, default=None,
    )

    def __str__(self):
        return self.text
    

class SubMenuLink(models.Model):
    class Meta:
        verbose_name = "Sub Menu(Produtos)"
        verbose_name_plural = "Sub Menus(Produtos)"

    text = models.CharField(max_length=100, verbose_name='Texto')
    url_or_path = models.CharField(max_length=250, default=None, null=True, blank=True)
    site_setup = models.ForeignKey(
        'SiteSetup', on_delete=models.CASCADE,
        blank=True, null=True, default=None,
        related_name='submenu_link'
    )

    def save(self, *args, **kwargs):
        if not self.url_or_path:
            self.url_or_path = f"/produtos/{slugify(self.text)}/"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.text


class SiteSetup(models.Model):
    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setups'

    title = models.CharField(max_length=65, verbose_name='Título')
    description = models.CharField(max_length=255, verbose_name='Descrição')
    favicon = models.ImageField(
        upload_to='assets/favicon/%Y/%m/',
        blank=True,
        default='',
        validators=[validate_png],
    )
    background_image = models.ImageField(
        upload_to='assets/background/%Y/%m',
        verbose_name='Background Imagem',
        blank=False,
        default='',
    )
    whatsapp_number = models.CharField(
        max_length=25,
        verbose_name="Número do Whatsapp",
        help_text="Inclua o código do país",
        validators=[
            RegexValidator(
                regex=r'^\+?\d+$',
                message='Digite apenas números, com ou sem + . Ex: +5521999999999'
            )
        ],
        default='',
        blank=False,
        null=False,
    )
    whatsapp_icon = models.ImageField(
        upload_to='assets/whatsapp_icon/%Y/%m/',
        verbose_name='Icone Whatsapp',
        blank=False,
        default='',
    )

    def save(self, *args, **kwargs):

        current_favicon_name = str(self.favicon.name)
        super().save(*args, **kwargs)
        favicon_changed = False

        check_favicon(self.favicon, current_favicon_name, favicon_changed)
        

    def __str__(self):
        return self.title
    

class Banner(models.Model):

    class Meta:
        ordering = ["order"]
        verbose_name = "Banner"
        verbose_name_plural = "Banners"

    title = models.CharField(max_length=255, blank=True, verbose_name='Título')
    description = models.CharField(max_length=500, default='', blank=True, verbose_name='Descrição')
    button_name = models.CharField(max_length=50, blank=True, verbose_name='Button Name')
    button_link = models.CharField(max_length=100, blank=True, verbose_name='Button Link')
    banner_img = models.ImageField(
        upload_to='assets/banners/%Y/%m', 
        blank=True, default='', verbose_name='Banner Imagem'
    )
    is_active = models.BooleanField(default=True, verbose_name='Ativo?')
    order = models. PositiveIntegerField(default=0, verbose_name='Ordem')
    site_setup = models.ForeignKey(
        'SiteSetup', on_delete=models.CASCADE,
        blank=True, null=True, default=None,
        related_name='banners',
    )

    def __str__(self):
        return self.title
    

class Contacts(models.Model):

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    time = models.CharField(max_length=255, default='', verbose_name="Horário")
    telephone_number_bonsucesso = models.CharField(max_length=55, default='', verbose_name="Número Telefone Fixo(Bonsucesso)")
    telephone_number_saocristovao = models.CharField(max_length=55, default='', verbose_name="Número Telefone Fixo(São Cristóvão)")
    email = models.CharField(max_length=65, default='', verbose_name="Email")
    whatsapp_number_footer = models.CharField(
        max_length=25,
        verbose_name="Número do Whatsapp para Footer",
        default='',
        blank=False,
        null=False,
    )
    address_bonsucesso = models.CharField(max_length=155, default='', verbose_name="Endereço Bonsucesso")
    address_bonsucesso_link = models.CharField(max_length=155, default='', verbose_name="Endereço Bonsucesso Link")

    address_saocristovao = models.CharField(max_length=155, default='', verbose_name="Endereço São Cristóvão")
    address_saocristovao_link = models.CharField(max_length=155, default='', verbose_name="Endereço São Cristóvão Link")

    instagram_url = models.URLField(default='', verbose_name="Instagram")
    facebook_url = models.URLField(default='', verbose_name="Facebook")

    site_setup = models.ForeignKey(
        'SiteSetup', on_delete=models.CASCADE,
        blank=True, null=True, default=None,
        related_name='contacts',
    )

    def __str__(self):
        return 'Gazil Equipamentos'