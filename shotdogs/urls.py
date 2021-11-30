from django.urls import path
from .views import (
    PhotoAllListView,
    HomeAllListView,
    Price_001_ListView
)

app_name = 'shotdogs'
urlpatterns = [
    path('', HomeAllListView.as_view(), name="home"),
    path('photo', PhotoAllListView.as_view(), name="photo"),
    path('price', Price_001_ListView.as_view(), name="price"),  
   
]

