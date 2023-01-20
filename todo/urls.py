from django.urls import path
from . import views
from rest_framework import routers
from .views import (AtDetailView, AtListView, CastleView, CpListView,
                    FlightCreateView, FlightMyListView, LocationView,
                    PfListView, PnListView, Price001ListView, Price002ListView,
                    Price003ListView, Price004ListView, PtListView,
                    ServiceListView, SgListView, StudioListView,
                    Wedding01ListView, Wedding02ListView, Wedding03ListView,
                    Wedding04ListView, WeddingDeleteView,
                    WeddingDetailView, WeddingListView,
                    WeddingUpdateView, YoutubeListView, FamilyListView, ApiForm001)

app_name = 'todo'
router = routers.DefaultRouter()
router.register('apiset', views.ApiForm001)

urlpatterns = [
    path('', WeddingListView.as_view(), name='list'),
    path('studio', StudioListView.as_view(), name='studio'),
    path('studio-yt', YoutubeListView.as_view(), name='yt'),
    path('service', ServiceListView.as_view(), name='service'),
    path('price001', Price001ListView.as_view(), name='price001'),
    path('price002', Price002ListView.as_view(), name='price002'),
    path('price003', Price003ListView.as_view(), name='price003'),
    path('price004', Price004ListView.as_view(), name='price004'),
    path('pn', PnListView.as_view(), name='pn'),
    path('sg', SgListView.as_view(), name='sg'),
    path('pf', PfListView.as_view(), name='pf'),
    path('cp', CpListView.as_view(), name='cp'),
    path('pt', PtListView.as_view(), name='pt'),
    path('at', AtListView.as_view(), name='at'),
    path('fam', FamilyListView.as_view(), name='fam'),
    path('detail/<int:pk>', AtDetailView.as_view(), name='detail'),
    path('wed-01', Wedding01ListView.as_view(), name='wed-01'),
    path('wed-02', Wedding02ListView.as_view(), name='wed-02'),
    path('wed-03', Wedding03ListView.as_view(), name='wed-03'),
    path('wed-04', Wedding04ListView.as_view(), name='wed-04'),
    path('location', LocationView.as_view(), name='loa'),
    path('castle', CastleView.as_view(), name='cas'),
    path('mylist', FlightMyListView.as_view(), name='mylist'),
    path('create', FlightCreateView.as_view(), name='create'),
    path('update/<int:pk>', WeddingUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', WeddingDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', WeddingDetailView.as_view(), name='detail'),
    path('list', views.weddinglistapi, name='list-api'),
]
