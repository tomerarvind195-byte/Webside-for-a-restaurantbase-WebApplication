from django.contrib import admin
from django.urls import path
from mainapp import views

urlpatterns = [
   path('', views.index, name='home'),
   path('contact/',views.contact, name='contact'),
   path('about/', views.about, name='about'),
   path('services/', views.services, name='services'),
   path('cart/', views.cart, name='cart'),
   path("order/<str:item>/", views.order_now, name="order_now"),
   path("feedback", views.feedback, name="feedback"),
   path("place-order/", views.place_order, name="place_order"),
   path("success/", views.order_success, name="order_success"),
 
]