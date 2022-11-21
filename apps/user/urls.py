from django.contrib import admin
from django.urls import re_path
from apps.user import views
from apps.user.views import register_view

urlpatterns = [
    re_path(r'^register', register_view.as_view(), name='register'),  #

]
