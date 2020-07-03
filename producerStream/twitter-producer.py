import json
from kafka import KafkaProducer, KafkaClient
import tweepy
import os

# Twitter Credentials Obtained from http://dev.twitter.com
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_key = os.environ['ACCESS_KEY']
access_secret = os.environ['ACCESS_SECRET']

# Words to track
WORDS = ["USA", "China", "Venezuela", "Rusia", "Brazil", "Iran", "Israel", "Germany", "Japan"]

class StreamListener(tweepy.StreamListener):
    # This is a class provided by tweepy to access the Twitter Streaming API.

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")

    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print("Error received in kafka producer " + repr(status_code))
        return True # Don't kill the stream

    def on_data(self, data):
        """ This method is called whenever new data arrives from live stream.
        We asynchronously push this data to kafka queue"""
        try:
            producer.send('tweetsTopic', data.encode('utf-8'))
        except Exception as e:
            print(e)
            return False
        return True # Don't kill the stream

    def on_timeout(self):
        return True # Don't kill the stream

# Kafka Configuration
producer = KafkaProducer(bootstrap_servers=['kafka:9093'])
# producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# Create Auth object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True, wait_on_rate_limit_notify=True, timeout=60, retry_delay=5, retry_count=10, retry_errors=set([401, 404, 500, 503])))
stream = tweepy.Stream(auth=auth, listener=listener)
stream.filter(track=WORDS, languages = ['en'])
