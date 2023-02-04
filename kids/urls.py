from django.urls import path
from .views import (
    Kid_AllListView, kid_salon, kid_oyoc, kid_pw, kid_nb
)

app_name = 'veronahuang'
urlpatterns = [
    path('', Kid_AllListView.as_view(), name="base_kid"),
    path('home', Kid_AllListView.as_view(), name="home_kid"),
    path('salon', kid_salon.as_view(), name="salon_kid"),
    path('oyoc', kid_oyoc.as_view(), name="oyoc_kid"),
    path('pw', kid_pw.as_view(), name="pw_kid"),
    path('nb', kid_nb.as_view(), name="nb_kid"),
]
