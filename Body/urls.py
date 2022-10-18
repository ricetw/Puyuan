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
from Body import views

urlpatterns = [
    path('/', views.user),
    path('/default/', views.userdefault),
    path('/setting/', views.usersetting),
    path('/blood/pressure/', views.bloodpressure),
    path('/weight/', views.weight),
    path('/blood/sugar/', views.bloodsuger),
    path('/records/', views.records),
    path('/medical/', views.medical),
    path('/a1c/', views.alc),
    path('/drug-used/', views.drug),
    path('/last-upload/', views.lastupload),
    path('/diary/', views.diary),
    path('/diet/', views.diet),
    path('/badge/', views.badge),
    path('/care/', views.care),
]
