# Generated by Django 5.1.2 on 2024-10-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon_scraper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.URLField(null=True, verbose_name='URL of the Product Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Product Name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=50, null=True, verbose_name='Stock Keeping Unit'),
        ),
    ]
