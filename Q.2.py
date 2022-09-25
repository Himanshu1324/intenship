#!/usr/bin/env python
# coding: utf-8

# # 2. Provide a program to read the CSV file.

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('data.csv')


# In[3]:


df = pd.DataFrame(data)


# In[4]:


df.insert(1,'age', True)

print(df)


# In[5]:


from datetime import datetime, date

born='20/06/2002'
print("Born :",born)

#Identify given date as date month and year
born = datetime.strptime(born, "%d/%m/%Y").date()

#Get today's date
today = date.today()

print("Age :",today.year - born.year - ((today.month,today.day) < (born.month,born.day)))


# In[6]:


file_path=input('by user')
print(file_path)


# In[ ]:




