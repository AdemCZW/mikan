from django.urls import path
from .views import (
    vh_index_ListView,
    vh_studio_ListView,
    vh_style_001_ListView,
    vh_style_002_ListView,
    vh_style_003_ListView,
    vh_style_004_ListView,
    vh_style_005_ListView,
    vh_style_006_ListView,
    vh_big_frds_ListView,
    vh_big_cpl_ListView,
    vh_big_single_ListView
)

app_name = 'veronahuang'
urlpatterns = [
    path('', vh_index_ListView.as_view(), name="verona"),
    path('studio', vh_studio_ListView.as_view(), name="studio"),
    path('style-1', vh_style_001_ListView.as_view(), name="style001"),
    path('style-2', vh_style_002_ListView.as_view(), name="style002"),
    path('style-3', vh_style_003_ListView.as_view(), name="style003"),
    path('style-4', vh_style_004_ListView.as_view(), name="style004"),
    path('style-5', vh_style_005_ListView.as_view(), name="style005"),
    path('style-6', vh_style_006_ListView.as_view(), name="style006"),
    path('frds', vh_big_frds_ListView.as_view(), name="frds"),
    path('cpl', vh_big_cpl_ListView.as_view(), name="cpl"),
    path('single', vh_big_single_ListView.as_view(), name="single"),
]