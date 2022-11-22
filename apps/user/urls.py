from django.contrib import admin
from django.urls import re_path
from apps.user import views
from apps.user.views import register_view, ActiveView, loginView

urlpatterns = [
    re_path(r'^register', register_view.as_view(), name='register'),  #
    re_path(r'^active/(?P<token>.*)', ActiveView.as_view(), name='active'),
    re_path(r'^login', loginView.as_view(), name='login'),
]
