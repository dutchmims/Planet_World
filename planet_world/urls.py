"""planet_world URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views as home_views  


from checkout.views import checkout_view, order_confirmation_view
from bag import urls as bag_urls

urlpatterns = [
    path('', home_views.index, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('profile/', home_views.profile_view, name='profile'),
    path('my-profile/', home_views.my_profile, name='my_profile'), 
    path('product_management/', home_views.product_management, name='product_management'),
    path('checkout/', checkout_view, name='checkout'),
    path('order_confirmation/', order_confirmation_view, name='order_confirmation'),
    path('bag/', include(bag_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
