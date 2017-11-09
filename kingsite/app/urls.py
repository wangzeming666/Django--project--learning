from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^herolist/', views.heroList),
    url(r'^heroDesc/(\d+)', views.heroDesc),
    url(r'^heroInsert/', views.heroInsert),
    url(r'^heroSkin/', views.heroSkin),
    url(r'^heroshow/', views.heros),
    url(r'^pic/', views.upload),
    url(r'^upload/', views.tryone),

]
