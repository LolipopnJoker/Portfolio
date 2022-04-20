"""WebS_3 - Scraping data from Twitter

In many cases, twits can be a useful data source. In this Python script I am scraping twits
from Twitter using tweepy package, cleaning and storing them in a database.
"""

__author__ = "Yoav Weller"
__copyright__ = "Copyright 2022, Yoav Weller"
__credits__ = ["Yoav Weller"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Yoav Weller"
__email__ = "yoav.weller@gmail.com"
__status__ = "Production"

# Imports
import tweepy
import configparser
import pandas as pd

class importing_twitts(object):
    """importing_twitts description
    
    As the discription of this document suggests, the main goal of this Pthon file is to scrape
    twits from Twitter.
    My main concern when building this class is making it powerful yet flexible - I want it to
    get as many data as I can, no matter how hard it would be to retrieve it.
    """
    
    def __init__(self):
        # Reading configs
        config = configparser.ConfigParser() # Creating config variable
        config.read('config.ini') # Reading the config file

        self.twitter_api_key = config['twitter']['api_key'] # Getting the Twitter API key
        self.twitter_api_key_secret = config['twitter']['api_key_secret'] # Getting the Twitter secret API key

        self.twitter_access_token = config['twitter']['access_token'] # Getting the Twitter access token
        self.twitter_access_token_secret = config['twitter']['access_token_secret'] # Getting the Twitter secret access token

        # Authentication
        self.auth = tweepy.OAuthHandler(self.twitter_api_key, self,self.twitter_api_key_secret)
        self.auth.set_access_token(self.twitter_access_token, self.twitter_access_token_secret)

        self.api = tweepy.API(auth=self.auth) # Connecting to the API
    
    def get_tweets(self, q, geocode, lang, locale, result_type, count, until, since_id, max_id, include_entities):
        
        self.tweet = self.api.search_tweets(q = q, geocode = geocode, lang = lang, locale = locale, result_type = result_type, count = count, until = until, since_id = since_id, max_id = max_id, include_entities = include_entities)

        return self.tweet
    
    def get_trendes(self):

        self.api.available_trends()