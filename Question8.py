#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#question 8
import pandas as pd

data = {
"A": [1, 2, 2, 1],
"B": [3.1, 4.2, 1.5, 6.3],
"C": [800, 150, 400, 210] }
newDataFrame=pd.DataFrame(data) # create a data frame
newDataFrame["D"]= newDataFrame["A"]*newDataFrame["B"]*newDataFrame["C"] #multiplying the columns together to get new column D
print(newDataFrame) # print the new data frame

