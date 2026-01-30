#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# question 1
Threshold_value=220
product=1 #start the product at 1 because if you start 0 it will never increase.
current_value=1 # start the current value at 1 for the same reason.
while product <= Threshold_value: # Keep multiplying until the product exceeds the threshold value
    product=product*current_value # multiply the product by the current value
    if product> Threshold_value:#  Stop the loop once the product exceeds the threshold to avoid extra increments
      break # when the product gets more then the threshold value we break from the loop.
    else:
        current_value=current_value+1

print(f"The final product is {product} the number that exceeded this threshold was {current_value}")

