from django.urls import path
from . import views

urlpatterns = [
    path('index-6', views.index6, name='index6'),
    path('index-7', views.index7, name='index7'),
    path('index-8', views.index8, name='index8'),
	path('cart/<' , views.cart , name= 'cart')
]
