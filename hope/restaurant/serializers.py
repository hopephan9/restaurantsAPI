from rest_framework import serializers

from hope.restaurant.models import Restaurant


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

