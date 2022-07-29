from django_filters import rest_framework as filters
from rest_framework import viewsets
from django.shortcuts import render

from hope.restaurant.models import Restaurant, MenuItem
from hope.restaurant.serializers import RestaurantSerializer, MenuItemSerializer


# def index(request):
# return render(request, 'index.html')

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = {'description': ['icontains'],
                        'name': ['icontains'],
                        'rating': ['gte', 'lt'],
                        'open': ['gt', 'lte'],
                        'close': ['gt', 'lte']}


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
