import numpy as np 
import pandas as pd 
import json
import sys
from ast import literal_eval
from tweet_analyzer import TweetAnalyzer


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage : parse_tweets.py [input json] [output csv] [append = true or False]")
    else:
        data = []
        csv_fname = sys.argv[2]
        append = sys.argv[3]
        with open(sys.argv[1], 'r') as text_json:
            for text in text_json:
                line = "[" + text + "]"
                data.append(line)
        print("File : ", sys.argv[1])        


        json_data = []
        tweet_count = 0
        for tweet in data:
            tweet_data = json.loads(tweet)
            if len(tweet_data) > 0:
                json_data.append(tweet_data[0])
                tweet_count += 1
                sys.stdout.write("\r" + str(tweet_count))
                sys.stdout.flush()
        print("\nTotal Tweets = ", len(json_data))

        tweet_analyzer = TweetAnalyzer()
        tweets_df = tweet_analyzer.convert_tweets_to_dataframe(json_data)
        tweet_analyzer.save_tweets_df_to_csv(fname = csv_fname, df = tweets_df, append_flag = append)
    
    print("Processing Done")
    