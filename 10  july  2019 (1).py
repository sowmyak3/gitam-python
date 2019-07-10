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


# In[1]:


li1=[1,2,3,4]
print("%d%d%d%d"%(li1[0],li1[1],li1[2],li1[3]))


# ### String Functions
# - upper()-- Will converts the given string into upper case
# - lower()-- Will converts the given string into lower case

# In[2]:


s1='Gitam'
print(s1.upper())
print(s1.lower())


# ### Boolean Function (True and False)
# - islower()-- True if the string is lower case/False if the string not in lower case
# - isupper()-- True if the string is upper case/False if the string not in upper case 
# - istitle()-- True if the string follows title case/ False
# - isalpha()-- True if the string contains only alphabets/False
# - isnumberic()--True if the string contains only numbers/False
# 

# In[4]:


s1='GITAM'
print(s1.islower())
print(s1.isupper())


# In[5]:


s2="Python Programming"
s3="python Programming"
print(s2.istitle())
print(s3.istitle())


# In[6]:


s2="Application1889"
s3="PythonProgramming"
print(s2.isalpha())
print(s3.isalpha())


# In[8]:


s1=" "
s2="Py th on"
print(s1.isspace())
print(s2.isspace())


# In[9]:


s1="1234"
s2="Application1234"
print(s1.isnumeric())
print(s2.isnumeric())


# ### String Methods
# - 1.join()-- Method will concatinates the two strings
# - 2.split()-- split() returns the a list of strings separted by whitespace(no parameters are given)
# - 3.replace()-- replaces the specific word/character with new word/character

# In[10]:


s1='Python'
print(" ".join(s1))


# In[11]:


li =['Python','Programming','Learn']
print(",".join(li))


# In[12]:


s2="Python Programming Easy to learn"
print(",".join(s2))


# In[13]:


s2="Python Programming Easy to learn"
print(s2.split())


# In[14]:


s2="Python Programming Easy to learn"
print(s2.split('a'))


# In[15]:


s2="Python Programming Easy to learn"
li=s2.split()
print(li)
print(len(li))


# In[16]:


s2="Python Programming Easy to learn"
li=list(s2)
print(li)


# In[17]:


s2="Python Programming Easy to learn"
print(s2.replace("gra","Application"))


# In[ ]:





# In[ ]:




