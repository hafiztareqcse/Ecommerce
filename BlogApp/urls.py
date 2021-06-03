from django.urls import path
from BlogApp import views

app_name = 'BlogApp'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('details/', views.blog_details, name='blog_details')
]
