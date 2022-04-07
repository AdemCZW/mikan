from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.contrib import auth
from .models import vh_index_001, vh_studio_001, vh_style_001, vh_style_002, vh_style_003, vh_style_004, vh_style_005, vh_style_006, vh_big_single, vh_big_cpl, vh_big_frds
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)



class vh_index_ListView(ListView):
    model = vh_index_001
    template_name = 'verona.html'  # 樣板路徑    

class vh_studio_ListView(ListView):
    model = vh_studio_001
    template_name = 'studio.html'  # 樣板路徑    

class vh_style_001_ListView(ListView):
    model = vh_style_001
    template_name = 'style-001.html'  # 樣板路徑    

class vh_style_002_ListView(ListView):
    model = vh_style_002
    template_name = 'article.html'  # 樣板路徑   

class vh_style_003_ListView(ListView):
    model = vh_style_003
    template_name = 'price.html'  # 樣板路徑    

class vh_style_004_ListView(ListView):
    model = vh_style_004
    template_name = 'article.html'  # 樣板路徑    

class vh_style_005_ListView(ListView):
    model = vh_style_005
    template_name = 'price.html'  # 樣板路徑    

class vh_style_006_ListView(ListView):
    model = vh_style_006
    template_name = 'article.html'  # 樣板路徑    

class vh_big_frds_ListView(ListView):
    model = vh_big_frds
    template_name = 'article.html'  # 樣板路徑    

class vh_big_cpl_ListView(ListView):
    model = vh_big_cpl
    template_name = 'price.html'  # 樣板路徑    

class vh_big_single_ListView(ListView):
    model = vh_big_single
    template_name = 'article.html'  # 樣板路徑    
# Create your views here.
