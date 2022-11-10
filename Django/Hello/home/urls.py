from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.base,name='Base'),
    path('index',views.index,name="index"),
    path('about',views.about,name='about'),
    path('contact', views.contact, name='contact'),
    path('Services', views.Services, name='services'),
    path('test', views.test, name='test'),
    path('jumbo', views.jumbo, name='jumbo')

]