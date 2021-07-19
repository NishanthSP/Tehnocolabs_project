from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index-2', views.index2, name='index2'),
    path('index-3', views.index3, name='index3'),
    path('index-4', views.index4, name='index4')
]
