import json

import tweepy
import requests

# import secrets from external file
with open("secrets.json","r") as file:
    secrets = json.load(file)

consumer_key = secrets["consumer_key"]
consumer_secret = secrets["consumer_secret"]
access_token = secrets["access_token"]
access_token_secret = secrets["access_token_secret"]

# create a Tweepy client
client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# get a random activity from boredapi
activity = requests.get('https://www.boredapi.com/api/activity').json()['activity']

tweet_text = "Cool Thing You Should Do Today" + "\n" + activity

# post the tweet using the Tweepy client
response = client.create_tweet(
    text=tweet_text
)

print('Finished tweeting')
