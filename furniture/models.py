from django.db import models
from djongo import models



class Popular_categories(models.Model):
    category_name = models.CharField(max_length=100)
    category_img = models.ImageField(upload_to = 'category')
    product_count = models.IntegerField()

class Hot_deals(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    image = models.ImageField(upload_to = 'furniture_product')
    design = models.TextField(default= 'STUDIO DESIGN')
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
    new_tag = models.BooleanField(default = False )
    availability = models.IntegerField()
    time_left = models.DateTimeField()

class products(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    image = models.ImageField(upload_to = 'furniture_product')
    design = models.TextField(default= 'STUDIO DESIGN')
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
    new_tag = models.BooleanField(default = False )

    best_seller = models.BooleanField(default = False )
    new_arrival = models.BooleanField(default = False )
    featured = models.BooleanField(default = False )
    home = models.BooleanField(default = False )
    office = models.BooleanField(default = False )
    outdoor = models.BooleanField(default = False )




class Latest_blogs(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'furniture_blogs')

class Slider_products(models.Model):
    header_1 = models.CharField(max_length=255)
    header_2 = models.CharField(max_length=255)
    header_3 = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'furniture_slider_products')

class Banner_products(models.Model):
    image = models.ImageField(upload_to = 'furniture_banner_products')

class Brand_logo(models.Model):
    logo_image = models.ImageField(upload_to = 'furniture_brand_logo')

