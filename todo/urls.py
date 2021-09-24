from django.urls import path
from .views import (
   
    WeddingListView,
    WeddingCreateView,
    WeddingUpdateView,
    WeddingDeleteView,
    WeddingDetailView,
    WeddingMyListView,
    StudioListView,
    ServiceListView,
    Price001ListView,Price002ListView,Price003ListView,Price004ListView,
    PnListView,SgListView,PfListView,CpListView,PtListView


)

app_name = 'todo'
urlpatterns = [
    path('', WeddingListView.as_view(), name='list'),
    path('studio', StudioListView.as_view(), name='studio'),


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

    path('mylist', WeddingMyListView.as_view(), name='mylist'),
    path('create', WeddingCreateView.as_view(), name='create'),
    path('update/<int:pk>', WeddingUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', WeddingDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', WeddingDetailView.as_view(), name='detail'),
   

]
