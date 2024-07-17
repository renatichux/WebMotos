"""
URL configuration for frontend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.home, name='post_list'),
    path('shop/', views.shop, name='post_list'),
    path('about/', views.info, name='post_list'),
    path('contact/', views.contact, name='post_list'),
    path('shopSingle/', views.shopSingle, name='post_list'),
    path('empleados/', views.empleados, name='post_list'),
    path('master/', views.master, name='post_list'),
    path('login/', views.login, name='post_list'),
    path('homeLogin/', views.homeLogin, name='post_list'),
    path('sucursales/', views.sucursales, name='post_list'),
    path('cliente/', views.cliente, name='post_list'),
    path('productos/', views.productos, name='post_list'),
    path('cargo/', views.cargo, name='post_list'),
    
]
