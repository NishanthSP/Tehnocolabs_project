from django.shortcuts import render


from .models import Popular_categories, Hot_deals, Slider_products, Banner_products, products, Latest_blogs, Brand_logo

def index13(request):
	best_seller = products.objects.filter(best_seller=True)
	popular_category = Popular_categories.objects.all()
	hot_deal = Hot_deals.objects.all()
	new_arrival = products.objects.filter(new_arrival=True)
	featured = products.objects.filter(featured=True)
	home = products.objects.filter(home=True)
	office = products.objects.filter(office=True)
	out_door = products.objects.filter(outdoor=True)


	latest_blog = Latest_blogs.objects.all()
	slider_product = Slider_products.objects.all()
	banner_product = Banner_products.objects.all()
	brand_logo = Brand_logo.objects.all()

	return render(request, "index-13.html", {'best_sellers': best_seller,
                                             'popular_categories':popular_category,
									'hot_deals': hot_deal,
									'new_arrivals':new_arrival,
									'featured':featured,
									'home': home,
	                                'offices' : office,
	                                'out_doors': out_door,
									'latest_blogs': latest_blog,
									'slider_products': slider_product,
									'banner_products': banner_product,
									'brand_logos': brand_logo})


def index14(request):
	best_seller = products.objects.filter(best_seller=True)
	popular_category = Popular_categories.objects.all()
	hot_deal = Hot_deals.objects.all()
	new_arrival = products.objects.filter(new_arrival=True)
	featured = products.objects.filter(featured=True)
	home = products.objects.filter(home=True)
	office = products.objects.filter(office=True)
	out_door = products.objects.filter(outdoor=True)

	latest_blog = Latest_blogs.objects.all()
	slider_product = Slider_products.objects.all()
	banner_product = Banner_products.objects.all()
	brand_logo = Brand_logo.objects.all()

	return render(request, "index-14.html", {'best_sellers': best_seller,
	                                         'popular_categories': popular_category,
	                                         'hot_deals': hot_deal,
	                                         'new_arrivals': new_arrival,
	                                         'featured': featured,
	                                         'home': home,
	                                         'offices': office,
	                                         'out_doors': out_door,
	                                         'latest_blogs': latest_blog,
	                                         'slider_products': slider_product,
	                                         'banner_products': banner_product,
	                                         'brand_logos': brand_logo})