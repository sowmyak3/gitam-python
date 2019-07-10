#!/usr/bin/env python
# coding: utf-8

# # Data Structures
# ### Dictionaries

# ### Dictionaries
# - It works on the concept of set unique data
# - Keys,Values is the unique identifier for a value
# - Each key annd value is separated by comma(,)
# - Dictionaries enclosed with curly braces({})

# In[3]:


d1={"Name":"Gitam","EmailId":"gitam@gmail.com","Address":"Hyderabad"}
print(d1)


# In[4]:


d1["Name"]


# In[8]:


d1['EmailId']='Gitam-Python@gmail.com' # Update the data


# In[9]:


d1['EmailId']


# In[11]:


del d1['EmailId'] # Delete the specific key value


# In[12]:


d1 # del d1 will delete the entire dict object


# In[13]:


d1.keys() #returns the list of keys


# In[14]:


d1.values() # return the values


# In[15]:


d1.items() # the list of tuples of keys and values


# ### Contact Application
# - Add Contact
# - Search the contact
# - List all contacts
#      - name1:phone1
#      - name2:phone2
# - Modify the contact
# - Remove the contact
# - Import the contact

# In[2]:


# Add contact
contacts ={} # Creating a dict object
def addcontact(name,phone):
    if name not in contacts:
        contacts[name] = phone
        print("Contact is details are added")
    else:
        print("Contact details are already exixts")
    return
addcontact('Rishi','7989333365')
addcontact('usa','8633546789')
addcontact('mad','7989701234')


# In[3]:


# Search for contact details
def searchcontact(name):
    if name in contacts:
        print(name,":",contacts[name])
    else:
        print("%s does not exists"%name)
    return
searchcontact('mad')
searchcontact('usha')
searchcontact('rishika')


# In[6]:


# Import some contacts
# Merge the contact with existing one
def importContact(newContacts):
    contacts.update(newContacts)
    print(len(newContacts.keys()),"Contacts added successfully")
    return
newContacts={'Rishika':7337687654,'usha':8919123456}
importContact(newContacts)


# In[7]:


contacts


# In[10]:


# Delete a contact
def deleteContact(name):
    if name in contacts:
        del contacts[name]
        print(name,"deleted successfully")
    else:
        print(name,"not exists")
    return
deleteContact('ush')


# In[11]:


contacts


# In[12]:


#Update the contact details
def deleteContact(name,phone):
    if name in contacts:
        contacts[name]=phone
        print(name,"Updated successfully")
    else:
        print(name,"Not exists")
    return
deleteContact('Rishi',7989333365)
deleteContact('ush',9848226200)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




