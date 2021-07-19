from django.db import models
from django.db.models.base import Model

from djongo import models


# Create your models here.

class Best_seller(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    image = models.ImageField(upload_to = 'organic_product')
    design = models.TextField(default= 'STUDIO DESIGN')
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
    new_tag = models.BooleanField(default = False )

class Popular_categories(models.Model):
    category_name = models.CharField(max_length=100)
    category_img = models.ImageField(upload_to = 'category')
    product_count = models.IntegerField()

class Hot_deals(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    image = models.ImageField(upload_to = 'organic_product')
    design = models.TextField(default= 'STUDIO DESIGN')
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
    new_tag = models.BooleanField(default = False )
    availability = models.IntegerField()
    time_left = models.DateTimeField()

class New_arrivals(models.Model):
    rating = models.IntegerField()
    image = models.ImageField(upload_to = 'organic_product')
    design = models.TextField(default= 'STUDIO DESIGN')
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
    new_tag = models.BooleanField(default = True )


class Featured_product(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    image = models.ImageField(upload_to = 'organic_product')
    design = models.TextField(default= 'STUDIO DESIGN')
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
    new_tag = models.BooleanField(default = False )

class Recently_added(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    image = models.ImageField(upload_to = 'organic_product')
    design = models.TextField(default= 'STUDIO DESIGN')
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
    new_tag = models.BooleanField(default = True )

class Slider_products(models.Model):
    header_1 = models.CharField(max_length=255)
    header_2 = models.CharField(max_length=255)
    header_3 = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'slider_products')

class Banner_products(models.Model):
    image = models.ImageField(upload_to = 'Banner_products')

class Brand_logo(models.Model):
    logo_image = models.ImageField(upload_to = 'Brand_logo')