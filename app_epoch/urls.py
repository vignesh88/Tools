from django.urls import path
from app_epoch import views

urlpatterns = [
    path('epoch.html', views.app_epoch, name='epoch'),
    path('ajax_epoch.html', views.app_epoch, name='epoch'),
    ]