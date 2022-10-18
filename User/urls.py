"""Puyuan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from User import views

urlpatterns = [
    path('register/', views.register),
    path('auth/', views.login),
    path('verification/send/', views.send),
    path('verification/check/', views.check),
    path('password/forgot/', views.forget_password),
    path('password/reset/', views.reset_password),
    path('register/check/', views.registercheck),
    path('share/', views.share),
    path('share/<type>/', views.seeshare),
    path('notification/', views.notification),
    path('news/', views.news),
]
