from django.contrib import admin

from .models import Tweet, TwitterConfiguration

admin.site.register(Tweet)
admin.site.register(TwitterConfiguration)
