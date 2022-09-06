from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('item_list/', views.item_list, name="item_list"),
    path('order_list/', views.order_list, name="order_list"),


]
