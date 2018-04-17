from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
    path('', views.order),
    path('addorder/', views.order_handle),
    url(r'^pay&(\d+)/$', views.pay),
]