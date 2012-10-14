import os
import settings
import tweepy

"""
Requirements:
    Env variables:
        TWITTER_CONSUMER_KEY
        TWITTER_CONSUMER_SECRET
        TWITTER_ACCESS_TOKEN
        TWITTER_ACCESS_TOKEN_SECRET
"""
class Twitter:
    def __init__(self):
        # == OAuth Authentication ==
        #
        # This mode of authentication is the new preferred way
        # of authenticating with Twitter.

        # The consumer keys can be found on your application's Details
        # page located at https://dev.twitter.com/apps (under "OAuth settings")
        self.__consumer_key = os.environ['TWITTER_CONSUMER_KEY'] 
        self.__consumer_secret = os.environ['TWITTER_CONSUMER_SECRET'] 

        # The access tokens can be found on your applications's Details
        # page located at https://dev.twitter.com/apps (located 
        # under "Your access token")
        self.__access_token = os.environ['TWITTER_ACCESS_TOKEN'] 
        self.__access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET'] 


        self.__auth = None
        self.__api = None
        self.__fetch_error = None

        # TODO: Wrap this in exception handler
        self.setAPI()

    def setAPI(self):
        self.__auth = tweepy.OAuthHandler(self.__consumer_key, self.__consumer_secret)
        self.__auth.set_access_token(self.__access_token, self.__access_token_secret)

        self.__api = tweepy.API(self.__auth)

        # If the authentication was successful, you should
        # see the name of the account print out
        #print self.__api.me().name

        # If the application settings are set for "Read and Write" then
        # this line should tweet out the message to your account's 
        # timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
        #api.update_status('Updating using OAuth authentication via Tweepy!')


    def latestTweet(self):
        """ Returns latest tweet from logged in users timeline """
        home_timeline = self.__api.home_timeline()
        return home_timeline[0]

