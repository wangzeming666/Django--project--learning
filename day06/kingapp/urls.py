
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^registe/$', views.registe),
    url(r'^login/$', views.login),
    url(r'^registe_handle/$', views.registe_handle),
    url(r'^login_handle/$', views.login_handle),
    url(r'^$', views.index),
    url(r'^product/(\d+)/$', views.product),
    url(r'^testfor/$', views.testfor),
]
