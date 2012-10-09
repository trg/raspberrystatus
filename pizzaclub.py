#!env python

import curses

# RaspberryStatus Modules
from brewskeeball import Brewskeeball
from util import Util

class PizzaClub:
    def __init__(self):
        self.__screen = None
        self.__brewskeeball = Brewskeeball()

    def printScreen(self):
        scn = self.__screen
        scn.clear()
        scn.border(0)

        # Title
        scn.addstr(0, 35, "PIZZA CLUB", curses.A_STANDOUT)

        # construct inner Window
        begin_x = 1 ; begin_y = 1
        height = 22 ; width = 78
        win = curses.newwin(height, width, begin_y, begin_x)

        # Menu
        menu_text = "press q to exit"
        win.addstr(height - 1, width - len(menu_text) - 1, menu_text)
        
        # Brewskeeball
        win.addstr(3, 0, Util.centerString("Next Matchup", width))
        win.addstr(5, 0, Util.centerString(self.__brewskeeball.matchupTeams(), width))
        win.addstr(7, 0, Util.centerString("%s at %s" % (self.__brewskeeball.matchupDate(), self.__brewskeeball.matchupTime()), width))
        
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
curses.wrapper( PizzaClub().mainLoop )

