from django.shortcuts import render
from .models import  digital_products , Popular_categories, Hot_deals,  Latest_blogs, Brand_logo, Slider_products, Banner_products
# Create your views here.

def index9(request):
    best_seller = digital_products.objects.filter(best_seller=True)
    popular_category = Popular_categories.objects.all()
    hot_deal = Hot_deals.objects.all()
    wearable_device = digital_products.objects.filter(wearable_device=True)
    smart_home_appliance = digital_products.objects.filter(smart_home_appliance=True)
    smart_remote_control = digital_products.objects.filter(smart_remote_control=True)
    headphone = digital_products.objects.filter(headphone=True)
    speaker = digital_products.objects.filter(speaker=True)
    mp3_player = digital_products.objects.filter(mp3_player=True)
    microphone = digital_products.objects.filter(microphone=True)

    latest_blog = Latest_blogs.objects.all()
    slider_product = Slider_products.objects.all()
    banner_product = Banner_products.objects.all()
    brand_logo = Brand_logo.objects.all()






    return render(request, "index-9.html", {'best_sellers': best_seller, 
                                             'popular_categories':popular_category,
									'hot_deals': hot_deal,
									'wearable_device':wearable_device,
									'smart_home_appliances':smart_home_appliance,
									'smart_remote_control': smart_remote_control,
									'headphones': headphone,
									'speakers': speaker,
									'mp3_players':mp3_player,
									'microphones':microphone,
									'latest_blogs': latest_blog,
									'slider_products': slider_product,
									'banner_products': banner_product,
									'brand_logos': brand_logo})

def index10(request):
    best_seller = digital_products.objects.filter(best_seller=True)
    popular_category = Popular_categories.objects.all()
    hot_deal = Hot_deals.objects.all()
    wearable_device = digital_products.objects.filter(wearable_device=True)
    smart_home_appliance = digital_products.objects.filter(smart_home_appliance=True)
    smart_remote_control = digital_products.objects.filter(smart_remote_control=True)
    headphone = digital_products.objects.filter(headphone=True)
    speaker = digital_products.objects.filter(speaker=True)
    mp3_player = digital_products.objects.filter(mp3_player=True)
    microphone = digital_products.objects.filter(microphone=True)

    latest_blog = Latest_blogs.objects.all()
    slider_product = Slider_products.objects.all()
    banner_product = Banner_products.objects.all()
    brand_logo = Brand_logo.objects.all()

    return render(request, "index-10.html", {'best_sellers': best_seller,
                                             'popular_categories':popular_category,
									'hot_deals': hot_deal,
									'wearable_device':wearable_device,
									'smart_home_appliances':smart_home_appliance,
									'smart_remote_control': smart_remote_control,
									'headphones': headphone,
									'speakers': speaker,
									'mp3_players':mp3_player,
									'microphones':microphone,
									'latest_blogs': latest_blog,
									'slider_products': slider_product,
									'banner_products': banner_product,
									'brand_logos': brand_logo})

def index11(request):
	best_seller = digital_products.objects.filter(best_seller=True)
	popular_category = Popular_categories.objects.all()
	hot_deal = Hot_deals.objects.all()
	wearable_device = digital_products.objects.filter(wearable_device=True)
	smart_home_appliance = digital_products.objects.filter(smart_home_appliance=True)
	smart_remote_control = digital_products.objects.filter(smart_remote_control=True)
	headphone = digital_products.objects.filter(headphone=True)
	speaker = digital_products.objects.filter(speaker=True)
	mp3_player = digital_products.objects.filter(mp3_player=True)
	microphone = digital_products.objects.filter(microphone=True)

	latest_blog = Latest_blogs.objects.all()
	slider_product = Slider_products.objects.all()
	banner_product = Banner_products.objects.all()
	brand_logo = Brand_logo.objects.all()

	return render(request, "index-11.html", {'best_sellers': best_seller,
                                             'popular_categories':popular_category,
									'hot_deals': hot_deal,
									'wearable_device':wearable_device,
									'smart_home_appliances':smart_home_appliance,
									'smart_remote_control': smart_remote_control,
									'headphones': headphone,
									'speakers': speaker,
									'mp3_players':mp3_player,
									'microphones':microphone,
									'latest_blogs': latest_blog,
									'slider_products': slider_product,
									'banner_products': banner_product,
									'brand_logos': brand_logo})

def index12(request):
	best_seller = digital_products.objects.filter(best_seller=True)
	popular_category = Popular_categories.objects.all()
	hot_deal = Hot_deals.objects.all()
	wearable_device = digital_products.objects.filter(wearable_device=True)
	smart_home_appliance = digital_products.objects.filter(smart_home_appliance=True)
	smart_remote_control = digital_products.objects.filter(smart_remote_control=True)
	headphone = digital_products.objects.filter(headphone=True)
	speaker = digital_products.objects.filter(speaker=True)
	mp3_player = digital_products.objects.filter(mp3_player=True)
	microphone = digital_products.objects.filter(microphone=True)

	latest_blog = Latest_blogs.objects.all()
	slider_product = Slider_products.objects.all()
	banner_product = Banner_products.objects.all()
	brand_logo = Brand_logo.objects.all()

	return render(request, "index-12.html", {'best_sellers': best_seller,
                                             'popular_categories':popular_category,
									'hot_deals': hot_deal,
									'wearable_device':wearable_device,
									'smart_home_appliances':smart_home_appliance,
									'smart_remote_control': smart_remote_control,
									'headphones': headphone,
									'speakers': speaker,
									'mp3_players':mp3_player,
									'microphones':microphone,
									'latest_blogs': latest_blog,
									'slider_products': slider_product,
									'banner_products': banner_product,
									'brand_logos': brand_logo})

def cart(request):
	if request.method == "POST":
		name = request.POST
