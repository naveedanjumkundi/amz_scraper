from celery import shared_task
from .models import brand, product
from .scraperx import *

@shared_task
def scraperz():
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
    
        
    return ()
@shared_task
def example():
    print('example task')

    return

