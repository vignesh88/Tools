from django.urls import path
from app_base64 import views

urlpatterns = [
    path('base64.html', views.app_base64, name='base64'),
    path('ajax_base64.html', views.app_base64, name='base64'),
    ]
