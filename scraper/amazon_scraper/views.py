from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import brand, product
from .scraperx import *

pnames = []
pASIN = []
pimg = []
temp = []
def home(request):
	brand_name = "Amazon Web Scraper"

	Companies = brand.objects.all()
	print('homeee')

	return render(request,'amazon_scraper/home.html', {
		"name":brand_name,
		"Companies":Companies,
		})


def amzscraper(request):
	brands = brand.objects.all()
	for cname in brands:
		(pASIN,pnames,pimg) = pagesx(10,cname)
		brobj = brand.objects.get(name=cname)
		for Pasin,name,img in zip(pASIN,pnames,pimg):
			if product.objects.filter(asin=Pasin).exists():
				pass
			else:
				p = product(name=name, asin=Pasin, image=img, brand=brobj)
				p.save()
	
	print('Scraper')
	
		
	return render(request,'amazon_scraper/scraper.html', {
		
		"productsASIN":pASIN,
		})

def product_view(request,pid):

	brand_obj = brand.objects.get(id=pid)

	products = product.objects.filter(brand=brand_obj)

	return render(request,'amazon_scraper/products.html', {
		
		"products":products,
		"brand":brand_obj,

		})
