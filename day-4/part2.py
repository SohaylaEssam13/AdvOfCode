#!/usr/bin/env python
# coding: utf-8

# In[1]:


the_cards = []

with open('sampleinput.txt') as f:
    for l in f:
        the_cards.append(l.rstrip())


# In[2]:


#numbers of cards
accumalative_number = []
for i in range(len(the_cards)):
    accumalative_number.append(1)


# In[3]:


win_card =" "
my_card = " "
the_intersection =0
points = 0
the_total_sum =0
for c, card in enumerate(the_cards):
    win_card, my_card = card.split('|')
    win_card = win_card[7:]
    the_intersection =set(win_card.split())& set(my_card.split())
    for i in range(len(the_intersection)):
        accumalative_number[c+i+1]+= accumalative_number[i]
        
for i in range(len(accumalative_number)):
    the_total_sum += accumalative_number[i]
print(the_total_sum )


    



# In[ ]:




