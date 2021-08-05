from .models import Flight
from django import forms
import django_filters
 
 
class FlightFilter(django_filters.FilterSet):

    items = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
 
    class Meta:
        model = Flight
        fields = {
            'items':['icontains'],
            }
