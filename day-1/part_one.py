#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


string_lists = []

with open('input.txt') as f:
    for l in f:
        string_lists.append(l)


# In[3]:


summation_List =[]
s=" "
count=0
number1 = 0 
number2 = 0
concat = " "
for i in range(len(string_lists)):
    s = string_lists[i]
    for j in s:
        if(j.isdigit()):
            count+=1
            if(count ==1):
                number1 = str(j)
                number2 = str(j)
            else:
                number2 = str(j)
    concat = number1 + number2        
    count = 0
    #print(number1, " ", number2 ," " ,concat)
    summation_List.append(int(concat))
    concat = " "  


# In[4]:


count =0
for i in range(len(summation_List)):
    count+= summation_List[i]
print(count)
#54916
#53334
#53651
    
        


# In[ ]:




