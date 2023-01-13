from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, LoginForm, CustomerModelForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import auth
from .models import Member, Flight, Index_001, Pn_001, Price_003, Price_004, Studio_001, Service_001, Price_001, Price_002, Price_003, Price_004, Pn_001, Sg_001, Pf_001, Cp_001, Pt_001, at_001, Wedding_01, Wedding_02, Wedding_03, Wedding_04, location_01, castle_01, youtube_studio, family_01, wedding_form_001
from .forms import FlightModelForm, IndexModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .filters import FlightFilter
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)


class FlightListView(ListView):
    model = Index_001
    queryset = Flight.objects.filter(finish=False)  # 指定查詢條件
    template_name = 'flight/flight_main.html'  # 樣板路徑

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(FlightListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = FlightFilter(
            self.request.GET, queryset=self.get_queryset())  # 資料模型表單
        return context


class FlightMyListView(LoginRequiredMixin, ListView):
    model = Index_001
    template_name = 'flight/flight_self.html'

    # 要傳遞的資料
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = IndexModelForm()  # 資料模型表單
        return context


class FlightCreateView(CreateView):
    model = Index_001
    form_class = IndexModelForm  # 使用的表單類別

    success_url = '/flight/mylist'  # 儲存成功後要導向的網址

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FlightCreateView, self).form_valid(form)
# wedding


class WeddingListView(ListView):
    model = Index_001
    template_name = 'flight/wedding_main.html'  # 樣板路徑


class StudioListView(ListView):
    model = Studio_001
    template_name = 'flight/studio.html'  # 樣板路徑


class ServiceListView(ListView):
    model = Service_001
    template_name = 'flight/service.html'  # 樣板路徑


class Price001ListView(ListView):
    model = Price_001
    template_name = 'flight/price-001.html'  # 樣板路徑


class Price002ListView(ListView):
    model = Price_002
    template_name = 'flight/price-002.html'  # 樣板路徑


class Price003ListView(ListView):
    model = Price_003
    template_name = 'flight/price-003.html'  # 樣板路徑


class Price004ListView(ListView):
    model = Price_004
    template_name = 'flight/price-004.html'  # 樣板路徑


class PnListView(ListView):
    model = Pn_001
    template_name = 'flight/pn-001.html'  # 樣板路徑


class SgListView(ListView):
    model = Sg_001
    template_name = 'flight/sg-001.html'  # 樣板路徑


class PfListView(ListView):
    model = Pf_001
    template_name = 'flight/pf-001.html'  # 樣板路徑


class CpListView(ListView):
    model = Cp_001
    template_name = 'flight/cp-001.html'  # 樣板路徑


class PtListView(ListView):
    model = Pt_001
    template_name = 'flight/pt-001.html'  # 樣板路徑


class AtListView(ListView):
    model = at_001
    template_name = 'flight/at-001.html'


class AtDetailView(DetailView):
    model = at_001
    template_name = 'flight/at_detail.html'


class Wedding01ListView(ListView):
    model = Wedding_01
    template_name = 'flight/wedding.html'  # 樣板路徑


class Wedding02ListView(ListView):
    model = Wedding_02
    template_name = 'flight/wedding_02.html'  # 樣板路徑


class Wedding03ListView(ListView):
    model = Wedding_03
    template_name = 'flight/wedding_03.html'  # 樣板路徑


class Wedding04ListView(ListView):
    model = Wedding_04
    template_name = 'flight/wedding_04.html'  # 樣板路徑


class LocationView(ListView):
    model = location_01
    template_name = 'flight/location.html'


class CastleView(ListView):
    model = castle_01
    template_name = 'flight/castle.html'


class YoutubeListView(ListView):
    model = youtube_studio
    template_name = 'flight/studio-yt.html'  # 樣板路徑


class FamilyListView(ListView):
    model = family_01
    template_name = 'flight/fam.html'  # 樣板路徑


class WeddingCreateView(CreateView):
    model = Index_001
    form_class = IndexModelForm  # 使用的表單類別

    success_url = '/flight/mylist'  # 儲存成功後要導向的網址

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WeddingCreateView, self).form_valid(form)


class WeddingUpdateView(UpdateView):
    model = Index_001
    form_class = IndexModelForm  # 使用的表單類別
    queryset = Index_001.objects.all()  # 這很重要
    template_name = 'flight/flight_update.html'  # 修改樣板
    success_url = '/flight/mylist'  # 儲存成功後要導向的網址

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


class WeddingDeleteView(DeleteView):
    model = Index_001
    template_name = 'flight/flight_delete.html'  # 刪除樣板
    success_url = '/flight/mylist'  # 刪除成功後要導向的網址


class WeddingDetailView(DetailView):
    model = Index_001
    template_name = 'flight/flight_detail.html'
