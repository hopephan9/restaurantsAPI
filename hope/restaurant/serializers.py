from rest_framework import serializers

from hope.restaurant.models import Restaurant, MenuItem


class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['item', 'price', 'restaurant', 'url']


class MenuItemObjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['item', 'price', 'url']


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    menuitem = MenuItemObjectSerializer(read_only=True, many=True)

    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'chain', 'rating', 'address', 'open', 'close', 'menuitem']
