from django.contrib import admin
from django.urls import re_path
from apps.user import views

urlpatterns = [
    re_path(r'^register_handle', views.register_handle, name='register_handle'),  #
    re_path(r'^register', views.register, name='register'),  #

]
