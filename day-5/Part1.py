#!/usr/bin/env python
# coding: utf-8

# In[1]:


the_data = []


# In[2]:


with open('sampleinput.txt') as f:
    for l in f:
        the_data.append(l.rstrip())


# In[3]:


temp = []
seeds =  []
data = []
sl =''
Find_the_location=[]
for i in the_data:
    if i.startswith('seeds:'):
        temp = i[6:].strip().split(' ')
        for s in (temp):
            seeds.append(int(s))
for s in seeds:
    los = s #the location of the seed
    for d in the_data:

        if ':' in d or d == '':
            continue
           
        num = d.split(' ')
        destination = int(num[0])
        source = int(num[1])
        length =int(num[2])
        if(los >= source and los<= source+length):
            los = destination +los - source
        
    Find_the_location.append(los)
    
print(Find_the_location)
        
            
            
                
                
            
                  


# In[ ]:




