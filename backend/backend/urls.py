"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from . import views
from .views_serializer import router
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('harrys/', admin.site.urls),
    path('ventas/', include('ventas.urls')),
    path('menuHarrys/', views.LoadMenu.as_view()),
    path('api/', include(router.urls)),
    path('', views.LoadMenu.as_view()),
    #path('/', views.LoadMenu.as_view()),
    path('front/', include('front.urls')),
]
