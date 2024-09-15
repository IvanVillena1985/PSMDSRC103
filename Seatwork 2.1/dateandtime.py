#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time 

def pause():
    for i in range(10, 0, -1): 
        print(f"The program will end in {i}...")
        time.sleep(1)


# In[ ]:





# In[2]:


def current_time(): 
    t = time.strftime("%I:%M %p")
    return t


# In[ ]:





# In[3]:


def current_date():
    d = time.strftime("%b %d %Y")
    return d


# In[ ]:





# In[ ]:




