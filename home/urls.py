from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # Add URL pattern for the profile page
    path('my-profile/', views.my_profile, name='my_profile'),
]
