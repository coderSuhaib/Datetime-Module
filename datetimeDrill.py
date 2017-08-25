# Python Ver: 2.7.13
#
# Author: Suhaib Al-Tamimi
#
# Purpose: Use datetime module to create code that uses current time (Portland) to find the
#          time in the NYC and London branches. Then use that time to check if the office are
#          open. hours of operation are from 9:00 A.M to 9:00 P.M
#
# Tested OS: This code was written and tested to work with mac OS 10.12.6.

from datetime import datetime

# first thing is find local time
locTime = datetime.now().strftime("%H")
# find portland time which is the current time, then find NYC time and London time.
#Then convert the hours into integers so they can be used in the function below.
pdxTime = int(locTime)
nycTime = int(locTime) + 3 # The pluse 3 is for the time difference in NYC
ldnTime = int(locTime) + 8 # The pluse 8 is for the time difference in London

print ('To check if the offices in New York City and London are open Enter:')

userInput = int(raw_input('1 for New York City or 2 for London: '))

officeOpen = 9
officeClose = 21

def open_hours():
    if userInput == 1:
        if nycTime > officeOpen and nycTime < officeClose:
            print ("NEW York City office is open")
        else:
            print ('New York City Office is closed')
    elif userInput == 2:
        if ldnTime > officeOpen and ldnTime < officeClose:
            print ("London office is open")
        else:
            print ('London Office is closed')
    else:
        print ('Incorrect selection!')
        
        
