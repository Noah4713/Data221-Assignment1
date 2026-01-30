#!/usr/bin/env python
# coding: utf-8

# In[1]:


#question 4
from random import random

values = [random() for i in range(20)] # the starter code
x = random()
ordered_values=sorted(values) # sort the values in the list as requested
count=0 # I am going to use count to find the index value
for i in ordered_values: 
    if i>= x: # if the value in the list is greater than x then we print the requested information and break from the loop
        print(ordered_values)
        print(f"The value x is {x}")
        print(f"The index value where x was exceeded is {count}")

        break
    else:count=count+1 # otherwise we are adding 1 to the count

if x > ordered_values[-1]: # this checks the last index in the sorted list as this is the greatest value
    print(ordered_values)
    print(f"The value x is {x}")


# In[ ]:




