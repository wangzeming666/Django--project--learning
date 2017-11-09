from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^index2', views.index2),
    url(r'^bash', views.bash)
    ]
