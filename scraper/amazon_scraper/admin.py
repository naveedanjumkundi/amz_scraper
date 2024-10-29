from django.contrib import admin

# Register your models here.
from .models import brand, product

#admin.site.register(Surah)
#admin.site.register(Ayah)

@admin.register(brand)
class brandAdmin(admin.ModelAdmin):
	list_display = ('name',)

@admin.register(product)
class productAdmin(admin.ModelAdmin):
	list_display = ('name', 'sku', 'asin')
	ordering = ('asin',)