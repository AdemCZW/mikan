from django.urls import path
from .views import (
    Kid_AllListView
)

app_name = 'veronahuang'
urlpatterns = [
    path('', Kid_AllListView.as_view(), name="base_kid"),
    path('home', Kid_AllListView.as_view(), name="home_kid"),
]