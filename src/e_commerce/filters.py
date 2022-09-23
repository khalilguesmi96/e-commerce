import django_filters
from django_filters import CharFilter
from django import forms
from .models import *


class ItemFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr="icontains",label="")


    class Meta:
        model = Item
        fields = ['title']