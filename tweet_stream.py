from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from twitter_credentials import api_credentials

class print_tweets(StreamListener):
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    tweet_filters = ["synagogueshooting", "pittsburg"]
    listener = print_tweets()

    cred = api_credentials()
    auth = OAuthHandler(cred.consumer_key, cred.consumer_secret)
    auth.set_access_token(cred.access_token, cred.access_token_secret)

    stream = Stream(auth, listener)

    stream.filter(track=tweet_filters)