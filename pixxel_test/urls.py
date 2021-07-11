"""pixxel_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from countries import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.CountryCreate.as_view(), name='create-country'),
    path('countries/', views.CountryList.as_view()),
    path('', views.CountryList.as_view()),
    path('countries/<int:pk>/', views.CountryDetail.as_view(), name='retrieve-country'),
    path('update/<int:pk>/', views.CountryUpdate.as_view(), name='update-country'),
    path('delete/<int:pk>/', views.CountryDelete.as_view(), name='delete-country'),
    path('india/intersection/', views.IntersectionViewOfIndia.as_view(), name='india_intersection'),
    path('spatial/intersection/', views.IntersectionView.as_view(), name='spatial_intersection'),

]
