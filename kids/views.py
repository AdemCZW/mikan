from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.contrib import auth
from .models import kid_index, kids_ph_salon, kids_ph_oyoc, kids_ph_pw, kids_ph_nb
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


class kid_salon(ListView):
    model = kids_ph_salon
    template_name = 'kid_salon.html'  # 樣板路徑


class kid_oyoc(ListView):
    model = kids_ph_oyoc
    template_name = 'kid_oyoc.html'  # 樣板路徑


class kid_pw(ListView):
    model = kids_ph_pw
    template_name = 'kid_pw.html'  # 樣板路徑


class kid_nb(ListView):
    model = kids_ph_nb
    template_name = 'kid_nb.html'  # 樣板路徑
