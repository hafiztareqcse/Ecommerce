from django.urls import path
from UserApp import views

app_name = 'UserApp'

urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('update/', views.user_update, name='user-update'),
    path('password/', views.password_change, name='password-change'),
    path('logout/', views.user_logout, name='logout'),
]
