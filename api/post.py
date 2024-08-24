import tweepy
import api.config as config
import time


client = tweepy.Client(consumer_key=config.api_key, 
                       consumer_secret=config.api_key_secret,
                       access_token=config.access_token,
                       access_token_secret=config.access_token_secret)

time_in_seconds = 2


def post_tweets_from_file(filename, interval=time_in_seconds):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        for line in lines:
            if ':' in line:
                key, tweet = line.split(':', 1)
                tweet = tweet.strip() 
                if tweet:
                    respone = client.create_tweet(text=tweet)
                    print(f" Tweet: {tweet}")
                    time.sleep(interval)
            else:
                print(f"Skipped invalid line: {line}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    
post_tweets_from_file('tweets.txt')




