#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = pd.read_csv('C:\\Users\\fadya\\Downloads\\new project.csv')


# In[3]:


data.isnull()


# In[4]:


data.isnull().sum()


# In[5]:


remove = ['Review ID','Date']
data.drop(remove, inplace =True, axis =1)


# In[6]:


data['Review'] = data['Review'].fillna('No review')


# In[7]:


data.duplicated()


# In[8]:


data.drop_duplicates()


# In[9]:


#5. Detect Outliers
data['Rating'].describe()


# In[10]:


data.loc[10,'Rating'] = 1


# In[11]:


#6. Normalize Casting
data['Review Title'] = data['Review Title'].str.lower()


# In[12]:


data['Customer Name'] = data['Customer Name'].str.title()


# In[13]:


data


# In[ ]:




