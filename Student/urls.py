from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('Login',views.Login,name="Login"),
    path('',views.Register,name="Register"),
    path('home',views.home,name='home'),
    path('logout', views.logout, name='logout')
]
