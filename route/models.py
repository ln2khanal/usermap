from __future__ import unicode_literals

from django.db import models


class Route(models.Model):
    """
    User's Route details
    """
    route_id = models.CharField(max_length=100)
    field_type = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()


class User(models.Model):
    """
    User's details
    """
    user_route = models.ForeignKey(Route, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
