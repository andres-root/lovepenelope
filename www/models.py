
from django.db import models


class Tweet(models.Model):
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    text = models.CharField(max_length=600)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    twitter_date_created = models.DateTimeField(blank=True)
    date_updated = models.DateTimeField(auto_now=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.text


class TwitterConfiguration(models.Model):
    account = models.CharField(max_length=200)
    consumer_key = models.CharField(max_length=200)
    consumer_secret = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)
    access_token_secret = models.CharField(max_length=200)
    topics = models.TextField()
    languages = models.TextField()
    geolocation = models.BooleanField(default=True)

    def __str__(self):
        return self.account


class Country(models.Model):
    country_name = models.CharField(max_length=200)
    country_code = models.CharField(max_length=2)
    topics = models.TextField()
    languages = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.country_name


class WelcomeMessage(models.Model):
    country_code = models.CharField(max_length=2)
    message = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.message
