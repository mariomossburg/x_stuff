# ***Access Only for Paid Plan***
# 
#  writing search queries
# https://github.com/xdevplatform/getting-started-with-the-twitter-api-v2-for-academic-research/blob/main/modules/5-how-to-write-search-queries.md

import tweepy
import api.config as config

client = tweepy.Client(bearer_token=config.bearer_token)

query = "nextjs OR react"

response = client.search_recent_tweets(query=query)


