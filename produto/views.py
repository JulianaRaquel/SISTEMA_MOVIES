from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from . import models

class home(ListView):
    model = models.Produto
    template_name = 'home.html'
    context_object_name = 'produtos'