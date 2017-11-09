from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index2/$', views.index2),
    url(r'^usercenter/$', views.usercenter),
    url(r'^userinfo/$', views.userinfo),
    url(r'^index3/$', views.index3),
    url(r'^csrf1/$', views.csrf1),
    url(r'^csrf2/$', views.csrf2),
    url(r'^csrf3/$', views.csrf3),
    url(r'^login/$', views.login),
    url(r'^verifyCode/$', views.verifyCode),
    url(r'^login_handle/$', views.login_handle),
]
