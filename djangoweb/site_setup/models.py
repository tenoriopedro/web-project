from django.db import models
from utils.model_validator import validate_png
from utils.images import resize_image


class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'

    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    site_setup = models.ForeignKey(
        'SiteSetup', on_delete=models.CASCADE,
        blank=True, null=True, default=None,
    )

    def __str__(self):
        return self.text
    

class SubMenuLink(models.Model):
    class Meta:
        verbose_name = "Sub Menu(Products)"
        verbose_name_plural = "Sub Menus (Products)"

    text = models.CharField(max_length=100)
    url_or_path = models.CharField(max_length=2048, default=None)
    site_setup = models.ForeignKey(
        'SiteSetup', on_delete=models.CASCADE,
        blank=True, null=True, default=None,
        related_name='submenu_link'
    )

class SiteSetup(models.Model):
    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setup'

    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    favicon = models.ImageField(
        upload_to='assets/favicon/%Y/%m/',
        blank=True,
        default='',
        validators=[validate_png],
    )

    def save(self, *args, **kwargs):

        current_favicon_name = str(self.favicon.name)
        super().save(*args, **kwargs)
        favicon_changed = False

        if self.favicon:
            favicon_changed = current_favicon_name != self.favicon.name

        if favicon_changed:
            resize_image(self.favicon, 64)


    def __str__(self):
        return self.title
    

class Banner(models.Model):

    class Meta:
        ordering = ["order"]
        verbose_name = "Banner"
        verbose_name_plural = "Banners"

    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=500, default='', blank=True)
    banner_img = models.ImageField(
        upload_to='assets/banners/%Y/%m', 
        blank=True, default='',
    )
    is_active = models.BooleanField(default=True)
    order = models. PositiveIntegerField(default=0)
    site_setup = models.ForeignKey(
        'SiteSetup', on_delete=models.CASCADE,
        blank=True, null=True, default=None,
        related_name='banners',
    )

    def __str__(self):
        return self.title