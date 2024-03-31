"""
URL configuration for E_tech_Bazzar project.

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
from django.urls import path,include
from customer import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base', views.base, name='base'),
    path('Home', views.index, name='Home'),
    path('About', views.About, name='About'),
    path('Contact', views.contact, name='Contact'),
    path('register', views.register, name='register'),
    path('login', views.loginPage, name='login'),
    path('shop', views.shop, name='shop'),
    path('Category', views.category, name='Category'),
    path('checkout', views.checkout, name='checkout'),
    path('Wish', views.wish, name='Wish'),
    # path('addCart/<str:slug>', views.addCart, name='addCart'),
    path('addCart/', views.addCart, name='addCart'),
    path('search', views.search, name='search'),
    path('logout', views.logoutPage, name='logout'),
    path('product/<str:slug>', views.product, name='product'),
]