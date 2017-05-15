""" Here's the actual UI for the organizer """
""" probably the most stupid interface ever designed """

import os
from UIUtils import *
from organizer import Organizer


# Splash screen and load organizer (or don't)
org = start()

# Exit value
exit = False

# Main Loop 

while not exit:
	exit = mainMenu(org)

clearScr()
