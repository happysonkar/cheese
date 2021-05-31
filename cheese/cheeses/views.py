from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Cheese
from django.contrib.auth.mixins import LoginRequiredMixin

class CheeseListView(ListView):
    model=Cheese

class CheeseDetailView(DetailView):
    model=Cheese
"""
class MyMixin(object):
    def some_method(self):
        return self.something
"""

class CheeseCreateView(LoginRequiredMixin,CreateView):
    fields=['name','description','firmness','country_of_origin']
    model=Cheese

