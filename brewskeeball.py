import urllib2
import re
from BeautifulSoup import BeautifulSoup

class Brewskeeball:
    def __init__(self, team_name="Pizza Club", league="nyc", day="Sunday"):
        self.__team_name = team_name
        self.__league = league
        self.__schedule_url = "http://brewskeeball.com/schedule/%s" % self.__league
        self.__day = day
        self.__fetch_error = None
        self.__soup = None
        
        self.getHtml()

    def getHtml(self):
        self.__fetch_error = None
        try:
            self.__soup = BeautifulSoup(urllib2.urlopen(self.__schedule_url).read())
        except Exception, e:
            self.__fetch_error = e
    
    def firstInnerTextWithString(self, search_string):
        if not self.__fetch_error:
            f = self.__soup.find(text=re.compile(search_string))
            if f != None:
                return f.strip()
            else:
                return "UNKNOWN"
        else:
            return "ERROR"

    """
    PUBLIC METHODS
    """

    def matchupTeams(self):
        return self.firstInnerTextWithString(self.__team_name)

    def matchupDate(self):
        return self.firstInnerTextWithString(self.__day)

    def matchupTime(self):
        matchup_time = "UNKNOWN"
        previous_element = self.__soup.find(text=re.compile(self.__team_name)).parent.parent.previousSibling
        while previous_element:
            if previous_element.find(text=re.compile(":00")) != None:
                matchup_time = previous_element.find(text=re.compile(":00"))
                return matchup_time
            previous_element = previous_element.previousSibling
        return matchup_time
