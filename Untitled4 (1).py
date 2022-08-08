#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd


# In[65]:


usr = pd.read_csv('/Users/ziyad/Downloads/instagram-users.csv')
usr


# In[66]:


usr.columns


# In[70]:


usr.index


# In[71]:


usr.values


# In[72]:


usr.T


# In[74]:


usr.dtypes


# In[75]:


usr.describe()


# In[76]:


usr.head()


# In[77]:


usr.tail()


# In[101]:


usr[usr['erl'].isnull()].head()


# In[102]:


usr.drop_duplicates()


# In[103]:


usr.T


# In[104]:


usr.columns = ['Num_posts', 'Num_following', 'Num_followers', 'Biography_length','Picture_availability','Link_availability','Average_caption_length','Caption_zero','Non_image_percentage','Engagement_rate_like','Engagement_rate_commen','Location_tag_percentage','Average hashtag count','Promotional keywords','Followers keywords','Cosine similarity','Post interval','real_fake']


# In[110]:


usr.rename(columns = {'f':'Fake', 'r':'Real'}, inplace = True)


# In[111]:


usr


# In[115]:


usr['real_fake']


# In[116]:


usr.describe()


# In[ ]:




