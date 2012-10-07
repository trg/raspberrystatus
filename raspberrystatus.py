#!env python

import curses

# RaspberryStatus Modules
from weather import Weather

class RaspberryStatus:
    def __init__(self):
        self.__screen = curses.initscr()
        self.__weather = Weather()

    def printScreen(self):
        scn = self.__screen
        scn.clear()
        scn.border(0)
        current_line = 0

        scn.addstr(1, 2, "Weather For Today")
        scn.addstr(2, 2, self.__weather.description())
        
        scn.refresh()

    def mainLoop(self):
        user_input = 0
        while user_input != ord('q'):
            self.printScreen()
            user_input = self.__screen.getch()
        curses.endwin()

# Main
rs = RaspberryStatus()
rs.mainLoop()
