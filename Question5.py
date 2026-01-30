#!/usr/bin/env python
# coding: utf-8

# In[1]:


#question 5
from math import pi
def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    if type(radiusOfCircle1)!=int or type(radiusOfCircle2)!=int:
        return("Both values must be positive integers")
    if radiusOfCircle1<=0 or radiusOfCircle2<=0:
            # this checks if either radius are negative values.
        return("Both values must be positive integers")


    areaOfCircle1=(pi*((radiusOfCircle1)**2)) # calculates the area given the radius.
    areaOfCircle2=(pi*((radiusOfCircle2)**2)) # calculates the area given the radius.
    if radiusOfCircle1 >= radiusOfCircle2:
        return f"Percentage covered by the smaller circle is {(areaOfCircle2 / areaOfCircle1)*100}" # checks the percentage covered if circle 1 is bigger
    else:
        return f"Percentage covered by the smaller circle is {(areaOfCircle1 / areaOfCircle2)*100}" # checks the percentage covered if circle 2 is bigger
print(circleAreaCoverage(1,2))


# In[ ]:




