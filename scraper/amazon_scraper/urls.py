from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name="home1"),
	path('amzscraper/', views.amzscraper, name="amz-scraper"),
	path('product_view/<int:pid>', views.product_view, name="product-view"),
]