from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'signup'

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
]