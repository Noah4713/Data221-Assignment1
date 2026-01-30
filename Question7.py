#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#question 7
def timeSinceMidnight(number):
    if number<0 or number >=86400: # number must be between 0 and 24 hours
        return"That is an invalid time."
    hour=(number//(60*60)) # check how many hours by finding the floor when divided by the number of seconds in a hour

    minute=((number%(60*60))//60) # use the remainder of seconds after divided b the amount of hours to find the amount of minutes in that hour

    seconds=(number %60) # use the remainder when divided by 60 to see the excess amount of seconds
    if hour==0: # make it so 12 am shows 12 am and not 0 am
        newHour=12 
        timeOfDay="AM"
    else:
        if hour>=12: # make the afternoon times say PM
            timeOfDay="PM"
            if hour>=13:
                newHour=hour-12 # make it so its a 12 hour clock not a 24 hour clock
            else:
                newHour=hour
        else:
            timeOfDay="AM"
            newHour=hour

    finalTime=(f"{newHour} {minute} {seconds} {timeOfDay}") # put it into a variable
    return finalTime
print(timeSinceMidnight(number=86399))

