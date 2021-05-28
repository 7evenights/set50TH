#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


url = "https://marketdata.set.or.th/mkt/sectorquotation.do?sector=SET50&language=th&country=TH"


# In[3]:


r = requests.get(url)


# In[4]:


html_page = BeautifulSoup(r.text, "html.parser")
html_page


# In[11]:


stat_table = html_page.find_all('table')
stat_table


# In[12]:


df = pd.read_html(str(stat_table))


# In[18]:


df[2]


# In[24]:


df[2].to_excel("set50.xlsx")


# In[ ]:




