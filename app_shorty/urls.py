from django.conf.urls import include, url, re_path
from django.urls import path
from app_shorty import views
from django.contrib import admin
from app_shorty.views import LinkCreate
from app_shorty.views import LinkShow
from app_shorty.views import RedirectToLongURL

urlpatterns = [
    re_path(r'^shorty$', LinkCreate.as_view(), name='home'),
    re_path(r'^shorty/link/(?P<pk>\d+)$', LinkShow.as_view(), name='link_show'),
    re_path(r'r/(?P<short_url>\w+)$', RedirectToLongURL.as_view(), name='redirect_short_url'),
]