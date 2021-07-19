from django.urls import path
from . import views

urlpatterns = [
    path('index-9', views.index9, name='index9'),
    path('index-10', views.index10, name='index10'),
    path('index-11', views.index11, name='index11'),
    path('index-12', views.index12, name='index12'),
	path('cart', views.cart, name='cart')
]
