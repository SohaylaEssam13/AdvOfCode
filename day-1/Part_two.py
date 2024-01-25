#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


numbers = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eigh":8, "nine":9}


# In[3]:


s = []
with open('input.txt') as f:
    for l in f:
        s.append(l)


# In[4]:


line = ' '
count = 0
number1 =0
number2 =0
the_total_number = ' '
list_of_numbers =[]
for i, l in enumerate(s):
    line =l
    print(line)
    for j in range(len(line)):
        if(line[j].isdigit()):
            if(count ==0):
                count+=1
                number1 = number2 = line[j]
            else:
                number2 = line[j]
        else:
            for x in numbers:
                if(line[j:].startswith(x)):
                    if(count ==0):
                        count+=1
                        number1 = number2 = numbers[x]
                    else:
                        number2 = numbers[x]
                    #print(numbers[x])
    print(number1, " ", number2)
    the_total_number = str(number1)+str(number2)
    list_of_numbers.append(the_total_number)
    count =0
                
            
        
    


# In[5]:


#for j in numbers:
   # print(j)
print(list_of_numbers)


# In[6]:


#for i, l in enumerate(s):
    #for j in numbers:
       # if(s[i:].startswith(j)):
           # print(numbers[j])


# In[7]:


x = y =2
print(x, y)


# In[8]:


#summation
summation = 0
for i in range(len(list_of_numbers)):
    summation += int(list_of_numbers[i])
print(summation)
    


# In[ ]:




