from django.urls import path
from OrderApp import views

app_name = 'OrderApp'

urlpatterns = [
    path('cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart-details/', views.cart_details, name='cart-details'),
    path('cart-delete/<int:id>/', views.cart_delete, name='cart-delete'),
    path('checkout/', views.order_cart, name='checkout'),
]
