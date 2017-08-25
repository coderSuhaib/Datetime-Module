import time

# first thing is find local time
locTime = time.localtime() 
# find portland time which is the current time, NYC time and London time. Then convert
# the hours into integers so then can be used in the function below.
pdxTime = int(locTime.tm_hour)
nycTime = int(locTime.tm_hour + 3)
ldnTime = int(locTime.tm_hour + 8)

print ('To check hours of operations in New York City and London type:')

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
        
        
open_hours()


    
