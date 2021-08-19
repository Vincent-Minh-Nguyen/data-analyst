#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv(".\Smart_City_index_headers.csv")


# In[4]:


df.head()


# In[5]:


df.describe()


# In[6]:


df.info


# In[8]:


df.isnull()


# In[13]:


df.columns


# In[24]:


white_space = df


# In[40]:


#Check and count number of whitespace in whole database

counter = 0

for column in df.columns:
    for i in column:
        check_white_space = i.isspace()
        if check_white_space == 1:            
            counter = counter + 1

print("Number of whitespace in whole dataset: ", counter)
    


# In[55]:


df.columns
new_headers = []

#Remove all whitespace

for column in df.columns:
    non_white_space_headers = column.rstrip()
    new_headers.append(non_white_space_headers)

print(new_headers)


# In[57]:


#Replace the old headers by new headers without spaces

df.columns = new_headers


# In[63]:


df.columns


# In[ ]:




