from django.urls import path
from .views import (
    PhotoAllListView,
    HomeAllListView
)

app_name = 'shotdogs'
urlpatterns = [
    path('', HomeAllListView.as_view(), name="home"),
    path('photo', PhotoAllListView.as_view(), name="photo"),  
   
]
