#!env python

import curses

# RaspberryStatus Modules
from weather import Weather
from brewskeeball import Brewskeeball
from twitter import Twitter
from util import Util

class RaspberryStatus:
    def __init__(self):
        self.__screen = None
        self.__weather = Weather()
        self.__brewskeeball = Brewskeeball()
        self.__twitter = Twitter()

    def printScreen(self):
        scn = self.__screen
        scn.clear()
        scn.border(0)

        # Title
        scn.addstr(0, 31, "RASPBERRY STATUS", curses.A_STANDOUT)

        # construct inner Window
        begin_x = 1 ; begin_y = 1
        height = 22 ; width = 78
        win = curses.newwin(height, width, begin_y, begin_x)

        # Weather
        win.clear()
        win.addstr(0, 0, "Weather For Today - Data provided by NOAA", curses.A_BOLD)
        weather_text = self.wordwrapStringAt(self.__weather.description() , width)
        win.addstr(1, 0, weather_text)
        win.hline( 3, 0, "-", width)

        # Brewskeeball
        win.addstr(4, 0, "Brewskeeball", curses.A_BOLD)
        win.addstr(5, 4, "Next Matchup:")
        win.addstr(6, 0, Util.centerString(self.__brewskeeball.matchupTeams(), width))
        win.addstr(7, 0, Util.centerString("%s at %s" % (self.__brewskeeball.matchupDate(), self.__brewskeeball.matchupTime()), width))
        win.hline( 8, 0, "-", width)

        # Twitter
        win.addstr(9,  0, Util.centerString("TWITTER @tom_g_", width), curses.A_BOLD)
        latest_tweet = self.__twitter.latestTweet()
        author_name = "@%s" % latest_tweet.author.screen_name
        win.addstr(10, 0, author_name, curses.A_BOLD)
        win.addstr(10, len(author_name)+1, latest_tweet.text )
        
        # Render screen
        scn.refresh()
        win.refresh()
    
    """
    Setup & Teardown Methods for the curses screen
    """
    def setupScreen(self, scr = None):
        curses.noecho()
        curses.cbreak()
        if scr:
            self.__screen = scr
        else:
            self.__screen = curses.initscr()
        self.__screen.keypad(1)
        curses.use_default_colors()


    def teardownScreen(self):
        curses.nocbreak()
        self.__screen.keypad(0)
        curses.echo()
        curses.endwin()

    def wordwrapStringAt(self, text, width):
        """ 
        Inject spaces into a string to cause curses to wordwrap at <width>
        BUG: Only does it for the first line.
        BUG: Untested
        """
        text = list(text)
        if len(text) > width:
            while text[width] != " ": # if last char isn't a space
                for x in range(0, width):
                    if text[width-x] == " ": # go backwards
                        text[width-x] = text[width-x] + " "
                        text = ''.join(text)
                        text = list(text)
                        break
        return ''.join(text)
            

    def mainLoop(self, stdscr):
        # Init Param from wrapper
        self.setupScreen(stdscr)
        user_input = 0
        while user_input != ord('q'):
            self.printScreen()
            user_input = self.__screen.getch()
        self.teardownScreen()
# Main
curses.wrapper( RaspberryStatus().mainLoop )
