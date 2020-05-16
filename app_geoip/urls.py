from django.urls import path
from app_geoip import views

urlpatterns = [
    path('geoip.html', views.app_geoip, name='geoip'),
    path('ajax_geoip.html', views.app_geoip, name='geoip'),
    ]
