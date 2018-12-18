#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import csv

ps = 'train.csv'

data = pd.read_csv(ps)


# In[ ]:





# In[7]:


len(data)


# In[8]:


data.head()


# In[10]:


data.count()


# In[12]:


data['Age'].min(), data['Age'].max()


# In[14]:


data['Survived'].value_counts()


# In[15]:


data['Survived'].value_counts()*100/len(data)


# In[17]:


data['Sex'].value_counts()


# In[18]:


data['Pclass'].value_counts()


# In[20]:


get_ipython().run_line_magic('matplotlib', 'inline')

alpha_color = 0.5

data['Survived'].value_counts().plot(kind='bar')


# In[21]:


data['Sex'].value_counts().plot(kind='bar',
                               color=['b','r'],
                               alpha=alpha_color)


# In[23]:


data['Pclass'].value_counts().sort_index().plot(kind='bar',alpha=alpha_color)


# In[24]:


data.plot(kind='scatter', x='Survived', y='Age')


# In[25]:


data[data['Survived']== 1]['Age'].value_counts().sort_index().plot(kind='bar')


# In[27]:


bins = [0, 10, 20, 30, 40, 50, 60, 70, 80]

data['AgeBin'] = pd.cut(data['Age'], bins)


# In[28]:


data[data['Survived'] == 1] ['AgeBin'].value_counts().sort_index().plot(kind='bar')


# In[29]:


data[data['Survived'] == 0] ['AgeBin'].value_counts().sort_index().plot(kind='bar')


# In[30]:


data[data['Pclass'] ==1]['Survived'].value_counts().plot(kind='bar')


# In[31]:


data[data['Pclass'] == 3]['Survived'].value_counts().plot(kind='bar')


# In[32]:


data[data['Pclass'] == 2]['Survived'].value_counts().plot(kind='bar')


# In[33]:


data[data['Sex'] == 'male']['Survived'].value_counts().plot(kind='bar')


# In[34]:


data[data['Sex'] == 'female']['Survived'].value_counts().plot(kind='bar')


# In[35]:


data[(data['Sex'] == 'male') & (data['Pclass'] == 1 )]['Survived'].value_counts().plot(kind='bar')


# In[36]:


data[(data['Sex'] == 'male') & (data['Pclass'] == 3 )]['Survived'].value_counts().plot(kind='bar')


# In[37]:


data[(data['Sex'] == 'female') & (data['Pclass'] == 1 )]['Survived'].value_counts().plot(kind='bar')


# In[38]:


data[(data['Sex'] == 'female') & (data['Pclass'] == 3 )]['Survived'].value_counts().plot(kind='bar')


# In[ ]:




