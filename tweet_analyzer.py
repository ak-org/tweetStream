
import pandas as pd 
import json
import io
from source_sanitize import parsed_values

class TweetAnalyzer():
    '''
    analyze tweets and convert it into a dataframe
    '''
    def convert_tweets_to_dataframe(self, json_data):
        df = pd.DataFrame(columns=['id', 'tweet_text', 'source','user_id','user_screen_name', 
                                   'user_follower_count','user_location', 'lang', 'timestamp_sec'])
        tweets_dict = {}
        for i in range(len(json_data)): #    len(tweets)  or 5 for testing
            ## print(json.dumps(json_data[i],indent = 2))
            if 'truncated' in json_data[i]:
                if json_data[i]['truncated'] == False:
                    tweet_text = json_data[i]['text']
                else:
                    tweet_text = json_data[i]['extended_tweet']['full_text']
                df.loc[i] = ([json_data[i]['id'],
                        tweet_text.replace('\n',''),  
                        parsed_values(json_data[i]['source']), 
                        json_data[i]['user']['id'],
                        json_data[i]['user']['screen_name'],
                        json_data[i]['user']['followers_count'],
                        json_data[i]['user']['location'],
                        json_data[i]['user']['lang'],
                        int(json_data[i]['timestamp_ms'])/100])
        return df
    def save_tweets_df_to_csv(self, fname, df, append_flag):
        if append_flag == False:
            with io.open(fname, 'w', encoding='utf-8', errors='replace') as f:
                df.to_csv(f, header=True, encoding='utf-8', index=False)
        else:
            with io.open(fname, 'a',encoding='utf-8', errors='replace') as f:
                df.to_csv(f, header=False, encoding='utf-8', index=False)         

