from django.contrib import admin
from .models import Best_seller, Popular_categories, Hot_deals, New_arrivals, Featured_product, Recently_added, Slider_products, Banner_products, Brand_logo

# Register your models here.

admin.site.register(Best_seller)
admin.site.register(Popular_categories)
admin.site.register(Hot_deals)
admin.site.register(New_arrivals)
admin.site.register(Featured_product)
admin.site.register(Recently_added)
admin.site.register(Slider_products)
admin.site.register(Banner_products)
admin.site.register(Brand_logo)

