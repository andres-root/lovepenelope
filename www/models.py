
from django.db import models


class Tweet(models.Model):
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    text = models.CharField(max_length=140)
    date_created = models.DateTimeField(auto_now_add=True)
    twitter_date_created = models.DateTimeField()
    date_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.text
