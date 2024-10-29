from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class brand(models.Model):
	name = models.CharField('Amazon Brand', max_length=50)


	def __str__(self):
		return self.name

class product(models.Model):
	name = models.CharField('Product Name', max_length=50, null=True)
	asin = models.CharField('ASIN', max_length=50, null=False)
	sku = models.CharField('Stock Keeping Unit', max_length=50, null=True)
	image = models.URLField('URL of the Product Image', max_length=200, null=True)
	brand = models.ForeignKey(brand, blank=False, null=False, on_delete=models.CASCADE)

