"""djangotodo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib.auth import views
from django.contrib import admin  
from todo import views
from shotdogs import views
from veronahuang import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('index/', include('todo.urls')),
    path('flight/', include('todo.urls')),
    path('wedding/', include('todo.urls')),
    path('shotdog/', include('shotdogs.urls')),
    path('verona/', include('veronahuang.urls')),
    path('kids/', include('kids.urls')),
]

