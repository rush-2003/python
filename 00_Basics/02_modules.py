import datetime
print(datetime.date.today())

# ____________________________________________________________________________

import os
print("Current working directory: {0}".format(os.getcwd()))
print (os.listdir())

# ____________________________________________________________________________

import pyfiglet
ascii_art = pyfiglet.figlet_format("I am learning python")
print(ascii_art)


