"""Proyectoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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


from django.contrib import admin
from django.urls import path
from Tienda import views



urlpatterns = [

    path('',views.home, name="home"),


    path('creardocente/', views.creardocente, name="creardocente"),
    path('modificardocente/<int:pk>', views.modificardocente, name="modificardocente"),
    path('eliminardocente/<int:pk>', views.eliminardocente, name="eliminardocente"),
    path('docentes/', views.docentes, name="docentes"),


    path('contact/',views.contact, name="contact"),
    path('portfolio/',views.portfolio, name="portfolio"),


]
