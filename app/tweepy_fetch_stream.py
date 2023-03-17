import unittest
import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

# load environment variables
bearer_token = os.getenv("BEARER_TOKEN")

# connect to tweepy client

client = tweepy.Client(bearer_token=bearer_token)

# Unit test class

query = 'DJIA lang:en -is:retweet'

for tweet in tweepy.Paginator(client.search_recent_tweets, query, tweet_fields="created_at,author_id,entities,public_metrics"):
    print(tweet)
    break


class TestStream(unittest.TestCase):
    def test_env(self):
        self.assertTrue(os.getenv("BEARER_TOKEN"))


if __name__ == "__main__":
    unittest.main()
