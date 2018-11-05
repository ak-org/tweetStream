from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from twitter_credentials import api_credentials

import sys

### Twitter Authenticator #### 
class TwitterAuthenticator():

    def auth_twitter_app(self):
        cred = api_credentials()
        auth = OAuthHandler(cred.consumer_key, cred.consumer_secret) 
        auth.set_access_token(cred.access_token, cred.access_token_secret)
        return auth

class TwitterStreamer():
    """
    Stream, Process and save tweets in a file
    """

    def __init__(self):
        self.twitter_authenticator = TwitterAuthenticator() 

    def stream_tweets(self, fname, tweet_filters):
        # This method authenticates, fetches tweets and save them in a file
        listener = save_tweets(fname)
        auth = self.twitter_authenticator.auth_twitter_app()
        
        
        stream = Stream(auth, listener)
        stream.filter(track=tweet_filters)
    

class save_tweets(StreamListener):
    """
    print tweets in a file
    """

    def __init__(self, fname):
        self.fname = fname
        self.tweet_count = 0

    def on_data(self, data):
        try:
            # print(data)
            self.tweet_count = self.tweet_count + 1
            sys.stdout.write("\r" + str(self.tweet_count))
            sys.stdout.flush()
                        ## break at 10K tweets    
            with open(self.fname, "a") as tf:
                tf.write(data)

            return True
        except BaseException as e:
            print("Error while streaming : %s" % str(e))
            return True

    def on_error(self, status):
        if status == 420:
            return False
        print(status)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : tweet_savefile.py <json file name>")
        print("If file already exists, new contents are appended to the end")
        exit
    else:
        tweet_filters = ["midterms", "midterm elections", "midterms elections", "republican", "democrat", "republicans", "democrats"]
        save_fname = sys.argv[1] ## expect a file name as first argument
        streamer = TwitterStreamer()
        streamer.stream_tweets(save_fname, tweet_filters)





   