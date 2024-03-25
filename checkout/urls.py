# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout_view, name='checkout'),
    path('order_confirmation/', views.order_confirmation_view, name='order_confirmation'),
]
