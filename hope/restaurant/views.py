from rest_framework import viewsets

from hope.restaurant.models import Restaurant
from hope.restaurant.serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
