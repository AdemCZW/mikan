from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.contrib import auth
from .models import kid_index
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)

class Kid_AllListView(ListView):
    model = kid_index
    template_name = 'kid_home.html'  # 樣板路徑    
