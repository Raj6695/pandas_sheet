#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import DataFrame


# In[82]:


import numpy as np
df1 = pd.read_csv("C:/Users/RAJ/Desktop/pandas (1)/jamesbond.csv")
df2 = pd.read_csv("C:/Users/RAJ/Desktop/pandas (1)/nba.csv")
df1["sport"]= "basketball"
df2["players"]= "nba"
df1.insert(3, column="league", value="nba")
# to join columns use this
info= pd.concat(objs= [df1,df2], axis =1 )

# to avoid NaN problem use this
df1.reset_index(drop=True, inplace=True)
df2.reset_index(drop=True, inplace=True)

info.loc[("movies",)]
info.loc[("players", 6), ["Name", "Height"]]


# info.to_csv("C:/Users/RAJ/Desktop/chk1.csv")
info


# In[64]:


df1 = pd.read_csv("C:/Users/RAJ/Desktop/pandas (1)/Restaurant - Customers.csv")
df2 = pd.read_csv("C:/Users/RAJ/Desktop/pandas (1)/Restaurant - Foods.csv")
df3 = pd.read_csv("C:/Users/RAJ/Desktop/pandas (1)/Restaurant - Week 1 Sales.csv")
df4 = pd.read_csv("C:/Users/RAJ/Desktop/pandas (1)/Restaurant - Week 1 Satisfaction.csv")
df5 = pd.read_csv("C:/Users/RAJ/Desktop/pandas (1)/Restaurant - Week 2 Sales.csv")


# In[68]:


info= pd.concat(objs= [df3,df5], keys= ["week1", "week2"] )
info


# In[100]:


data1= df3[["Customer ID", 'Food ID']]

data2= df5[["Customer ID", 'Food ID',]]


# In[101]:


dataframes=[data1, data2]


# In[104]:


join= pd.concat(dataframes)
join.reset_index(drop=True, inplace=True)


# In[90]:


# join.to_csv("C:/Users/RAJ/Desktop/chk3.csv")


# In[112]:


df3 = pd.read_csv("C:/Users/RAJ/Desktop/pandas (1)/Restaurant - Week 1 Sales.csv")
df5 = pd.read_csv("C:/Users/RAJ/Desktop/pandas (1)/Restaurant - Week 2 Sales.csv")
info= pd.concat(objs= [df3,df5], keys= ["week1", "week2"] )
info


# In[111]:


df3.merge(df5, how= "inner", on= "Customer ID")


# In[116]:


df3[df3["Customer ID"]==155]


# In[119]:


merged=df3.merge(df5, how= "outer", on= "Customer ID", indicator= True)
merged


# In[120]:


merged["_merge"].value_counts()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




