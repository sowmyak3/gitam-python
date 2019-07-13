#!/usr/bin/env python
# coding: utf-8

# ### Tranforming Code into Idiomatic Python
# - Replace traditional index manupulation with Python core looping idiomatic

# In[1]:


#Looping over a range of numbers-Traditional Approch
for i in [0,1,2,3,4,5]:
    print(i**2,end=" ")


# In[2]:


#Idiomatic Programming
for i in range(6):
    print(i**2,end=" ")


# ### Looping Over a Collection

# In[3]:


colors=['red','green','yellow','purple']
for i in range(len(colors)):
    print(colors[i],end=" ")


# In[4]:


for color in colors:
    print(color,end=" ")


# ### Looping backwards

# In[5]:


colors=['red','green','yellow','purple']
for i in range(len(colors)-1,-1,-1):
    print(colors[i],end=" ")


# In[6]:


for color in reversed(colors):
    print(color,end=" ")


# ### Looping in Sorted List

# In[7]:


colors=['red','green','yellow','purple']
for color in sorted(colors):
    print(color,end=" ")


# In[8]:


colors=['red','green','yellow','purple']
for color in sorted(colors,reverse=True):
    print(color,end=" ")


# ###
# - if x<=y and y<=z:
# - if x<=y<=z:
# - if x==True:
# - if x:
# 

# ### Pandas
# 

# In[9]:


import pandas as pd


# In[10]:


dt={'Id':[11,12,13,14,15],
  'first_name':['A','B','C','D','E'],
  'company':['aa','bb','cc','dd','ee'],
  'address':['Hyd','Hyd','Hyd','Hyd','Hyd']}
mydt=pd.DataFrame(dt)


# In[14]:


print(mydt)


# In[16]:


import os


# In[17]:


os.chdir("D:\\MyData\\")# Saves to certian location


# In[21]:


mydt.to_csv('WorkingFile.csv',index=False)


#   ### Reading the data from CSV file
# 

# In[22]:


mydata=pd.read_csv('workingFile.csv')


# In[23]:


print(mydata)


# In[24]:


mydata1=pd.read_csv('WorkingFile.csv',skiprows=1,
                   names=["CustId","Name","Company","Address"])


# In[25]:


print(mydata1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




