#!/usr/bin/env python
# coding: utf-8

# In[2]:


# question2
def structure_finder(list_of_strings):
    Dictonary_of_structure={} # make a empty dictionary so we can add to it later
    for i in (list_of_strings):# iterates over every item in the list
        length_of_string=len(i) # checks the length of the string
        if length_of_string%2==0: # checks for the remainder when divided by 2 to see if its odd or even
            Parity_of_string="even"
        else:
            Parity_of_string="odd"

        Dictonary_of_structure[i]={"length" : length_of_string, "parity": Parity_of_string} # this makes it so there are dictionaries within the bigger dictionary
    return Dictonary_of_structure
print(structure_finder(list_of_strings=["data","science","blue"]))


# In[ ]:




