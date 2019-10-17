"""Rental_management_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('equipment/',include('equipment.urls','equipment')),
    path('rental/', include('rental.urls', 'rental')),
    path('accounts/',include('django.contrib.auth.urls')),
<<<<<<< HEAD
# <<<<<<< HEAD
    path('accounts/', include('signup.urls', 'signup')),
# =======
#     path('signin/', register)
# >>>>>>> 33c1eb452f33419e85fbd20e0b4ba4c94d27c6b2
=======
    path('signin/', register, name='signin')
>>>>>>> acfc40f71c9fbe03555eab2b36a321c3eea7c3ef
]
