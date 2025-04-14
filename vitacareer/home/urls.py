from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login', views.user_login, name='user_login'),
    path('dashboard', views.user_details, name='user_details'),
    path('users/', views.users_list),
]