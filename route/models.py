from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    """
    User's details
    """
    user_key = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        """
        prints the object itself
        """
        return self.first_name + ' - ' + self.user_key


class Route(models.Model):
    """
    User's Route details
    """
    route_key = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True)
    field_type = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        """
        prints the object itself
        """
        return self.route_key + " - " + self.field_type
