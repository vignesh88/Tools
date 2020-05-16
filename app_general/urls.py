from django.urls import path
from app_general import views

urlpatterns = [
    path('', views.app_general, name='general'),
    path('ajax_general.html', views.app_general, name='general'),
    
    
    
    ]
