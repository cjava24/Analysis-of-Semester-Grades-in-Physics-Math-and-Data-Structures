#!/usr/bin/env python
# coding: utf-8

# In[3]:

# Import Python Libraries
import numpy as np
import pandas as pd


# In[6]:

# Load the Dataset 
data = pd.read_csv('PhysicsScoreTerm1.csv')
df = pd.DataFrame(data)
data1 = pd.read_csv('MathScoreTerm1.csv')
df1 = pd.DataFrame(data1)
data2 = pd.read_csv('DSScoreTerm1.csv')
df2 = pd.DataFrame(data2)


# In[14]:

# Print the Dataframe of the Physics Score Term 1 to view the data 
df


# In[20]:

# Delete the Name column for Physics Score Term 1 dataset
del(df['Name'])


# In[21]:

# Print the dataframe of the Physics Score Term 1
print(df)


# In[22]:

# Delete the name column from the third dataframe of the Data Structures Score Term 1 dataset
del(df2['Name'])


# In[23]:

# Delete the Ehtinicity column from the third dataframe of the Data Structures Score Term 1 dataset
del(df2['Ethinicity'])


# In[24]:

# Delete the Name and Enthinicity columns from the second dataframe of the Math Score Term 1 dataset
del(df1['Name'])
del(df1['Ethinicity'])


# In[25]:

# Print the second dataframe
df1


# In[26]:

# Print the third dataframe
df2


# In[66]:


# Filling in missing values of the first dataframe with 0
df.fillna(0)


# In[79]:

# Filling in missing values of second dataframe with 0
df1.fillna(0)


# In[65]:


# Filling in missing values of the third dataframe with 0
df2.fillna(0)


# In[73]:


# merging all dataframes together
list1 = [df,df1,df2]
dffinal = pd.concat(list1)


# In[77]:


# Splitting Gender Column by half the size
dffinal.groupby('Sex').head(300)


# In[78]:


# Storing data in new file
dffinal.to_csv('ScoreFinal.csv')

