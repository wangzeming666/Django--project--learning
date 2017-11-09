
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^hai/', views.sayHai),
    url(r'(\d+)/' ,views.detail),
    ]
