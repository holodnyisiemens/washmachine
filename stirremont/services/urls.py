from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('more/', views.more_info, name='more_info'),
    path('services/<slug:service_slug>/', views.about_service, name='services'),
]
