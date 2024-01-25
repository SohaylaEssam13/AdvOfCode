#!/usr/bin/env python
# coding: utf-8

# In[1]:


the_cards = []

with open('sampleinput.txt') as f:
    for l in f:
        the_cards.append(l.rstrip())


# In[2]:


win_card =" "
my_card = " "
the_intersection =0
points = 0
for card in the_cards:
    win_card, my_card = card.split('|')
    win_card = win_card[7:]
    the_intersection =set(win_card.split())& set(my_card.split())
    if (len(the_intersection )> 0):
        points += 2**(len(the_intersection)-1)

print(points)

    


# In[ ]:





# In[ ]:




