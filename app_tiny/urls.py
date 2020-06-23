from django.conf.urls import re_path, include, url
from app_tiny import views

urlpatterns = [
    re_path(r'^tiny$', views.home, name='home'),
    re_path(r'^tiny/(?P<id>\w+)$', views.link, name="link"),
    re_path(r'^tiny/(?P<id>\w+)/stats$', views.stats, name="stats"),
]
