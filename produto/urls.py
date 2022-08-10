from django.contrib import admin
from django.urls import path
from produto.views import home

urlpatterns = [
    path('', home.as_view(), name='home'),
]