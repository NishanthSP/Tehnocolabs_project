from django.contrib import admin

# Register your models here.
from .models import  Popular_categories, Hot_deals, products,  Latest_blogs, Brand_logo, Slider_products, Banner_products

# Register your models here.
admin.site.register(products)
admin.site.register(Popular_categories)
admin.site.register(Hot_deals)

admin.site.register(Latest_blogs)
admin.site.register(Brand_logo)
admin.site.register(Banner_products)
admin.site.register(Slider_products)