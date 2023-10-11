from django.shortcuts import render
from django.views import generic
from .models import Jobs,Category
# Create your views here.

class ProductList(generic.ListView):
    model = Jobs

