from django.urls import path
from . import views

urlpatterns = [
    path('index-13', views.index13, name='index13'),
    path('index-14', views.index14, name='index14')
]
