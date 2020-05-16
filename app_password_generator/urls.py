from django.urls import path
from app_password_generator import views

urlpatterns = [
    path('password_generator.html', views.app_password_generator, name='password_generator'),
    path('ajax_password_generator.html', views.app_password_generator, name='password_generator'),
    ]