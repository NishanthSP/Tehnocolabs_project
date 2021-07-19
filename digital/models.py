from django.db import models

from djongo import models


# Create your models here.

class Popular_categories(models.Model):
    category_name = models.CharField(max_length=100)
    category_img = models.ImageField(upload_to = 'category')
    product_count = models.IntegerField()

class Hot_deals(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    image = models.ImageField(upload_to = 'digital_product')
    design = models.TextField(default= 'STUDIO DESIGN')
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
    new_tag = models.BooleanField(default = False )
    availability = models.IntegerField()
    time_left = models.DateTimeField()

class digital_products(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    image = models.ImageField(upload_to = 'digital_product')
    design = models.TextField(default= 'STUDIO DESIGN')
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
    new_tag = models.BooleanField(default = False )

    best_seller = models.BooleanField(default = False )
    wearable_device = models.BooleanField(default = False )
    smart_home_appliance = models.BooleanField(default = False )
    smart_remote_control = models.BooleanField(default = False )
    headphone = models.BooleanField(default = False )
    speaker = models.BooleanField(default = False )
    mp3_player = models.BooleanField(default = False )
    microphone = models.BooleanField(default = False )





class Latest_blogs(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'digital_blogs')

class Slider_products(models.Model):
    header_1 = models.CharField(max_length=255)
    header_2 = models.CharField(max_length=255)
    header_3 = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'digital_slider_products')

class Banner_products(models.Model):
    image = models.ImageField(upload_to = 'digital_banner_products')

class Brand_logo(models.Model):
    logo_image = models.ImageField(upload_to = 'digital_brand_logo')


class cart_products(models.Model):
    name = models.CharField(max_length=100)
    # rating = models.IntegerField()
    image = models.ImageField(upload_to = 'digital_product_cart')
    # design = models.TextField(default= 'STUDIO DESIGN')
    # cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    # discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)
    # new_tag = models.BooleanField(default = False )




# class Best_seller(models.Model):
#     name = models.CharField(max_length=100)
#     rating = models.IntegerField()
#     image = models.ImageField(upload_to = 'digital_product')
#     design = models.TextField(default= 'STUDIO DESIGN')
#     cost_price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount_price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
#     new_tag = models.BooleanField(default = False )


# class Wearable_devices(models.Model):
#     name = models.CharField(max_length=100)
#     rating = models.IntegerField()
#     image = models.ImageField(upload_to = 'digital_product')
#     design = models.TextField(default= 'STUDIO DESIGN')
#     cost_price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount_price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
#     new_tag = models.BooleanField(default = False )

# class Smart_home_appliances(models.Model):
#     name = models.CharField(max_length=100)
#     rating = models.IntegerField()
#     image = models.ImageField(upload_to = 'digital_product')
#     design = models.TextField(default= 'STUDIO DESIGN')
#     cost_price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount_price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
#     new_tag = models.BooleanField(default = False )

# class Smart_remote_control(models.Model):
#     name = models.CharField(max_length=100)
#     rating = models.IntegerField()
#     image = models.ImageField(upload_to = 'digital_product')
#     design = models.TextField(default= 'STUDIO DESIGN')
#     cost_price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount_price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
#     new_tag = models.BooleanField(default = False )

# class Headphones(models.Model):
#     name = models.CharField(max_length=100)
#     rating = models.IntegerField()
#     image = models.ImageField(upload_to = 'digital_product')
#     design = models.TextField(default= 'STUDIO DESIGN')
#     cost_price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount_price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
#     new_tag = models.BooleanField(default = False )

# class Speakers(models.Model):
#     name = models.CharField(max_length=100)
#     rating = models.IntegerField()
#     image = models.ImageField(upload_to = 'digital_product')
#     design = models.TextField(default= 'STUDIO DESIGN')
#     cost_price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount_price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
#     new_tag = models.BooleanField(default = False )

# class Mp3_playes(models.Model):
#     name = models.CharField(max_length=100)
#     rating = models.IntegerField()
#     image = models.ImageField(upload_to = 'digital_product')
#     design = models.TextField(default= 'STUDIO DESIGN')
#     cost_price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount_price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
#     new_tag = models.BooleanField(default = False )

# class Microphones(models.Model):
#     name = models.CharField(max_length=100)
#     rating = models.IntegerField()
#     image = models.ImageField(upload_to = 'digital_product')
#     design = models.TextField(default= 'STUDIO DESIGN')
#     cost_price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount_price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount_percent = models.DecimalField(max_digits=10, decimal_places=2)
#     new_tag = models.BooleanField(default = False )
