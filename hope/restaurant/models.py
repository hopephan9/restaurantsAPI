from django.db import models
from django.forms import JSONField
# from mapped_fields import fields


class MenuItem(models.Model):
    number = models.AutoField(primary_key=True)
    item = models.CharField(max_length=100)
    price = models.FloatField()
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, null=False, related_name='menuitem')

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    chain = models.BooleanField(default=False)
    # menu = models.JSONField()
    rating = models.IntegerField()
    address = models.CharField(max_length=100)
    open = models.TimeField()
    close = models.TimeField()
    # latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    # longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
