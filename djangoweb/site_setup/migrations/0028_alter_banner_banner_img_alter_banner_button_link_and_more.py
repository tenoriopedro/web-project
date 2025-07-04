# Generated by Django 5.2.1 on 2025-05-24 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0027_alter_sitesetup_whatsapp_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_img',
            field=models.ImageField(blank=True, default='', upload_to='assets/banners/%Y/%m', verbose_name='Banner Imagem'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='button_link',
            field=models.CharField(blank=True, max_length=100, verbose_name='Button Link'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='button_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Button Name'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='description',
            field=models.CharField(blank=True, default='', max_length=500, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Orde,'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='menulink',
            name='text',
            field=models.CharField(max_length=50, verbose_name='Texto'),
        ),
        migrations.AlterField(
            model_name='sitesetup',
            name='description',
            field=models.CharField(max_length=255, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='sitesetup',
            name='title',
            field=models.CharField(max_length=65, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='submenulink',
            name='text',
            field=models.CharField(max_length=100, verbose_name='Texto'),
        ),
    ]
