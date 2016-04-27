
# from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from .api import Twitter
from .models import Tweet


def index(request):
    try:
        twitter = Twitter()
        topics = ['love', '#love']
        languages = ['en']
        twitter.stream(topics, languages)
        tweets = Tweet.objects.all()
        tweet = tweets[len(tweets) - 1]
        tweet_object = {
            'name': tweet.name,
            'user': tweet.user,
            'text': tweet.text,
            'date': tweet.twitter_date_created.strftime('%d/%b/%Y      %H:%M'),
            'error': False
        }
        return JsonResponse(tweet_object, safe=False)
    except Exception:
        tweet_object = {
            'name': '@Penelope',
            'user': 'Penelope',
            'text': 'I can\'t find you love.',
            'date': datetime.now().strftime('%d/%b/%Y      %H:%M'),
            'error': True
        }
        return JsonResponse(tweet_object, safe=False)
