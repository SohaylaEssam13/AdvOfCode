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


the_out_put = np.zeros((len(string), 5))


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
            if(st[i+3] =='b' and number> cb):
                cb=number
            elif(st[i+3]=='r' and number > cr):
                cr=number
            elif(st[i+3]=='g' and number > cg):
                cg=number
                
        elif(st[i].isdigit() and st[i+1].isdigit()==False and st[i-1].isdigit()==False):
            
            if(st[i+2]=='b' and int(st[i])> cb):
                cb=int(st[i])
            elif(st[i+2]=='r' and int(st[i])> cr):
                cr=int(st[i])
            elif(st[i+2]=='g' and int(st[i])> cg):
                cg=int(st[i])
    print(cb, "\t", cr,"\t", cg)
    the_out_put[j][0] = j+1
    the_out_put[j][1] = cb
    the_out_put[j][2] = cr
    the_out_put[j][3] = cg
    
    cb =0
    cr=0
    cg=0


# In[6]:


mutli = []
mv= 1
summationOFallgames =0
for i in range(len(string)):
    for j in range(1,4):
        mv*= the_out_put[i][j]
    print(mv)
    summationOFallgames+= mv
    the_out_put[i][4]= mv
    mv =1

print('All summation', summationOFallgames)
    


# In[7]:


the_presentation_of_data = pd.DataFrame(the_out_put, columns =['Game ID', 'Blue   ', 'Red', 'Green','Total summation'])
the_presentation_of_data


# In[ ]:




