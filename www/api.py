
from .models import Tweet, TwitterConfiguration
import tweepy


class StreamListener(tweepy.StreamListener):

    def __init__(self):
        super().__init__()
        self.counter = 0
        self.limit = 1

    def on_status(self, status):
        if self.counter < self.limit:
            self.counter += 1
            tweet_text = ''
            if hasattr(status, 'retweeted_status'):
                try:
                    tweet_text = status.retweeted_status.extended_tweet['full_text']
                except:
                    tweet_text = status.retweeted_status.text
            else:
                try:
                    tweet_text = status.extended_tweet['full_text']
                except AttributeError:
                    tweet_text = status.text

            tweet = Tweet(
                name=status.author.name,
                user=status.author.screen_name,
                text=tweet_text,
                twitter_date_created=status.created_at
            )
            tweet.save()
        else:
            return False

    def on_error(self, status_code):
        return False

    def on_timeout(self):
        return False


class Twitter(object):

    def __init__(self):

        conf = TwitterConfiguration.objects.first()
        self.consumer_key = conf.consumer_key
        self.consumer_secret = conf.consumer_secret
        self.access_token = conf.access_token
        self.access_token_secret = conf.access_token_secret
        self.api_auth = None
        self.api = None
        self.api_stream = None

    def auth(self):
        self.api_auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.api_auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.api_auth)
        return self.api

    def stream(self, topics, languages):
        self.auth()
        self.api_stream = tweepy.Stream(auth=self.api.auth, listener=StreamListener(), tweet_mode='extended')
        self.api_stream.filter(track=topics, languages=languages)
