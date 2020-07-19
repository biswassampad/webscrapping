#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup


# In[4]:


url = "https://biography.yourdictionary.com/articles/how-did-bruce-lee-die.html"
response = requests.get(url)
response


# In[5]:


soup = BeautifulSoup(response.text,'html.parser')


# In[ ]:





# In[9]:


paragraph=soup.p.text
paragraph


# In[10]:


updated_para = paragraph + '-parsed-'
updated_para


# In[16]:


# getting all the paragraphs
all_para = soup.findAll('p')


# In[23]:


for i in all_para:
         print(i.text)

