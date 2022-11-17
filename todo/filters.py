from .models import Flight
from django import forms
import django_filters


class FlightFilter(django_filters.FilterSet):

    items = django_filters.CharFilter(

        widget=forms.Select(choices=(('', '請選擇'),) + Flight.items_choices, attrs={'class': 'form-control'}))

    class Meta:
        model = Flight
        fields = {
            'items'
        }
