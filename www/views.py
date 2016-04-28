
import json
from django.http import HttpResponse
from .api import Twitter
from datetime import datetime
from .utils import get_client_ip
from .models import Tweet, TwitterConfiguration
from django.contrib.gis.geoip2 import GeoIP2


def index(request):
    try:
        ip = get_client_ip(request)
        g = GeoIP2()
        if ip == '127.0.0.1':
            country = 'localhost'
        else:
            country = g.city(ip)
        conf = TwitterConfiguration.objects.first()
        twitter = Twitter()
        topics = conf.topics.split()
        languages = conf.languages.split()
        twitter.stream(topics, languages)
        tweets = Tweet.objects.all()
        tweet = tweets[len(tweets) - 1]
        tweet_object = {
            'name': tweet.name,
            'user': '@{0}'.format(tweet.user),
            'text': tweet.text,
            'date': tweet.twitter_date_created.strftime('%d/%b/%Y      %H:%M'),
            'error': False,
            'country': country,
        }
        context = json.dumps(tweet_object, ensure_ascii=False)
        return HttpResponse(context, content_type="application/json;charset=utf-8")
    except Exception:
        ip = get_client_ip(request)
        g = GeoIP2()
        if ip == '127.0.0.1':
            country = 'localhost'
        else:
            country = g.city(ip)
        tweet_object = {
            'name': '@Penelope',
            'user': 'Penelopé',
            'text': 'I can\'t find you love.',
            'date': datetime.now().strftime('%d/%b/%Y \t \t \t \t \t \t \t %H:%M'),
            'country': country,
            'error': True
        }
        context = json.dumps(tweet_object, ensure_ascii=False)
        return HttpResponse(context, content_type="application/json;charset=utf-8")
