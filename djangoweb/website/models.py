from django.db import models 


class FeaturedProducts(models.Model):

    class Meta:
        verbose_name = "Featured Product"
        verbose_name_plural = "Featured Products"

    title = models.CharField(max_length=300, blank=True)
    description = models.CharField(max_length=1000, default='', blank=True)
    button_name = models.CharField(max_length=50, blank=True)
    button_link = models.CharField(max_length=100, blank=True)
    image = models.ImageField(
        upload_to='assets/featured_products/%Y/%m', 
        blank=True, default='',
    )

    def __str__(self):
        return self.title