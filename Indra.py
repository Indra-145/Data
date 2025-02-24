#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd


# In[12]:


data = pd.read_csv('vgchartz-2024.csv')


# In[14]:


data.head()


# In[16]:


data.info()


# In[18]:


data.describe()


# In[20]:


data.head(10)


# In[ ]:


isnull() is used to identify or detect the missing values in the data frame.


# In[22]:


data.isnull()


# In[ ]:


dropna() returns a new DataFrame object with rows or columns removed if they contain NA values.


# In[24]:


data.dropna()


# In[ ]:


fillna() replaces the NULL values with a specified value.


# In[26]:


data.fillna(10)


# In[ ]:


Creating total_sales column


# In[38]:


cols=['na_sales','jp_sales','pal_sales','other_sales']
data['total_sales']=data[cols].sum(axis=1)


# In[40]:


data


# In[ ]:


Computing the mean, median, and standard deviation for total sales


# In[32]:


import numpy as np


# In[42]:


mean_val = np.mean(data['total_sales'])
median_val = np.median(data['total_sales'])
std_val = np.std(data['total_sales'])
print(mean_val)
print(median_val)
print(std_val)


# In[ ]:


Filter records based on specific criteria : select rows where a total sales exceeds 13


# In[66]:


filtered_data = data[data['total_sales'] > 13]
filtered_data


# In[ ]:


Create a histogram to show the distribution of a total_sales


# In[44]:


import matplotlib.pyplot as plt
plt.hist(data['total_sales'], bins=20, color='green')
plt.title('Distribution of Numeric Column')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()


# In[ ]:


Generate a scatter plot to analyze the relationship between two numerical variables


# In[50]:


plt.scatter(data['other_sales'], data['pal_sales'],color='darkblue', alpha=0.2)
plt.title('pal_sales vs other_sales')
plt.xlabel('other_sales')
plt.ylabel('pal_sales')
plt.show()


# In[ ]:




