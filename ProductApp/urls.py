from django.urls import path
from ProductApp import views

app_name = 'ProductApp'

urlpatterns = [
    path('details/<int:id>/', views.product_single, name='singe-product'),
    path('category/<int:id>/<slug:slug>', views.category_product, name='category-product'),
    path('comment/<int:id>/', views.comment_add, name='comment'),
]
