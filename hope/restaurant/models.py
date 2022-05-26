from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    decription = models.CharField(max_length=100)
    rating = models.IntegerField()
    address = models.CharField(max_length=100)
    open = models.TimeField()
    close = models.TimeField()
