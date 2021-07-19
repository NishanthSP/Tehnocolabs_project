from django.shortcuts import render
from django.http import HttpResponse
from .models import Best_seller, Hot_deals, Popular_categories, New_arrivals, Featured_product, Recently_added, Slider_products, Banner_products, Brand_logo
# Create your views here.

def index(request):

	best_seller  = Best_seller.objects.all()
	popular_category = Popular_categories.objects.all()
	hot_deal = Hot_deals.objects.all()
	new_arrival = New_arrivals.objects.all()
	featured_product = Featured_product.objects.all()
	recently_added = Recently_added.objects.all()
	slider_product = Slider_products.objects.all()
	banner_product = Banner_products.objects.all()
	brand_logo = Brand_logo.objects.all()

	return render(request, "index.html", {'best_sellers': best_seller,
	                                      'popular_categories': popular_category, 
										  'hot_deals': hot_deal, 
										  'new_arrivals': new_arrival,
										   'featured_products': featured_product, 
										   'recently_added': recently_added,
										   'slider_products': slider_product,
										    'banner_products': banner_product,
											'brand_logos': brand_logo }
										)

def index2(request):
	return render(request, "index-2.html")

def index3(request):
	return render(request, "index-3.html")

def index4(request):
	return render(request, "index-4.html")