#!/usr/bin/env python
# coding: utf-8

# In[1]:


# question 3
def exponent(x,y):

    if y <0: # this checks if y is negative and skips it as requested
        return None

    else:
        result=x**y # this evaluates x to the power of y
        return result
pairs = [[5, 2], [3, -1], [4, 3], [2, 0]] # a example input
Final_result=[] #empty list so I can append later

for i in pairs:
    result=exponent(*i) #this applies the condition to each pair
    if result is not None: # we dont want results with a negative value as we already made - y values set to return none
        Final_result.append(result)
print (Final_result)


# In[ ]:




