import pywunder
import os
import settings

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
        self.__fetch_error = None

        self.getForcast()


    def getForcast(self):
        """ 
        Hits the Wunderground API for the latest forcast 
        Use to refresh the data from the server.
        """
        self.__fetch_error = None
        if not settings.DEBUG:
            try:
                self.__forcast = self.__client.forecast(self.__location)
            except Exception, e:
                self.__fetch_error = e

    def description(self):
        if not settings.DEBUG:
            if not self.__fetch_error:
                return self.__forcast[0].description
            else:
                return str(self.__fetch_error.message)
        else:
            return "Debug is true.  Overcast with rain in the evening, then partly cloudy with a chance of rain. Low of 8C. Winds from the WNW at 10 to 15 km/h. Chance of rain 70%."

    def __str__(self):
        return str(self.description)
