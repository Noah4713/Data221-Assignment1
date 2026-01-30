#!/usr/bin/env python
# coding: utf-8

# In[21]:


#question 6
def Distribution_Analysis(numbers):

    newNumbers=sorted(numbers) #sort the numbers in the list
    length=len(newNumbers)# check the length so we know how many items in the list
    Dictonary_of_Distribution_Analysis={}# make a  empty dictionary
    for i in (newNumbers):
        if i in Dictonary_of_Distribution_Analysis:
                    continue #skip if already exists
        count=0


        for x in (newNumbers): 
            if i>=x:
                count=count+1# check how many numbers the number is greater than
        percentage=((count/length)*100) # calculate the percentage of numbers less than x
        Dictonary_of_Distribution_Analysis[i]=percentage
    return Dictonary_of_Distribution_Analysis

print(Distribution_Analysis(numbers = [3, 1, 2, 3, 4, 2]))

