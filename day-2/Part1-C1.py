#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


string = []


# In[3]:


with open('input.txt') as f:
    for l in f:
        string.append(l)


# In[4]:


the_out_put = np.zeros((len(string), 4))


# In[5]:


st=""
number = 0
concat =' '
cb =0
cr=0
cg=0
for j in range(len(string)):
    st = string[j]
    print(st)
    for i in range(8,len(st)):
        if(st[i].isdigit() and st[i+1].isdigit()):
            concat = st[i] +  st[i+1]
            number = int(concat)
            if(st[i+3] =='b'):
                cb+=number
            elif(st[i+3]=='r'):
                cr+=number
            elif(st[i+3]=='g'):
                cg+=number
                
        elif(st[i].isdigit() and st[i+1].isdigit()==False and st[i-1].isdigit()==False):
            
            if(st[i+2]=='b'):
                cb+=int(st[i])
            elif(st[i+2]=='r'):
                cr+=int(st[i])
            elif(st[i+2]=='g'):
                cg+=int(st[i])
    print(cb, "\t", cr,"\t", cg)
    the_out_put[j][0] = j+1
    the_out_put[j][1] = cb
    the_out_put[j][2] = cr
    the_out_put[j][3] = cg
    
    cb =0
    cr=0
    cg=0
   
    
            
    


# In[6]:


the_out_put


# In[7]:


the_data = pd.DataFrame(the_out_put, columns = ['Game ID', 'blue', 'red', 'green'])
the_data


# In[8]:


#The restrictions are 12 red cubes, 13 green cubes, and 14 blue cubes
flage = True
limit = [14, 12,13]
summation=0
accepted_indices = []
for i in range(len(string)):
    flage = True
    if(the_out_put[i][1] > limit[0]):
        flage = False
    if(the_out_put[i][2] > limit[1]):
        flage = False
    if(the_out_put[i][3] > limit[2]):
        flage = False
    if(flage == True):
        accepted_indices.append(the_out_put[i][0])

accepted_indices
for i in accepted_indices:
    summation += i
print(int(summation))


# In[ ]:




