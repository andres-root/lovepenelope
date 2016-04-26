
from django.db import models


class Tweet(models.Model):
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    text = models.CharField(max_length=140)
    date = models.CharField(max_length=140)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.text
