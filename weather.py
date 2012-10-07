import pywunder
import os

"""
Requirements:
    Environment Variable: WUNDERGROUND_API_KEY
"""
class Weather:
    def __init__(self):
        
        self.__station = "KNYC"
        self.__client = pywunder.Client(os.environ['WUNDERGROUND_API_KEY'])
        self.__location = "11211"
        self.__forcast = None

        self.getForcast()


    def getForcast(self):
        """ 
        Hits the Wunderground API for the latest forcast 
        Use to refresh the data from the server.
        """
        self.__forcast = self.__client.forecast(self.__location)

    def description(self):
        return self.__forcast[0].description

    def __str__(self):
        return str(self.description)
