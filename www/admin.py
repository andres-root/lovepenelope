from django.contrib import admin

from .models import Tweet, TwitterConfiguration, Country

admin.site.register(Tweet)
admin.site.register(TwitterConfiguration)
admin.site.register(Country)
