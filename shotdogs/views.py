from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.contrib import auth
from .models import Shotdogs_photo, Home, Price, article
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)



class PhotoAllListView(ListView):
    model = Shotdogs_photo
    template_name = 'photo_001.html'  # 樣板路徑    

class HomeAllListView(ListView):
    model = Home
    template_name = 'home.html'  # 樣板路徑    

class Price_001_ListView(ListView):
    model = Price
    template_name = 'price.html'  # 樣板路徑    

class article_001_ListView(ListView):
    model = article
    template_name = 'article.html'  # 樣板路徑    







