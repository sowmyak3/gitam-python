#!/usr/bin/env python
# coding: utf-8

# ### Standard Libraries
# - File I/O
# - Regular Expression
# - Datetime
# - Math(numerical and Mathematical)

# ### File Handling in Python
# - File:- Document containing information resides on the permanent storage
# - Different types of files:-txt,doc,pdf,csv and etc..
# - Input -- Keyboard
# - Output -- File
# ### Modes of the File I/O
# - 'w' -- This mode is used to file writing
#       -- If the file is not present first it creates the file and write so me data to it
#        -- If the File is already present then it will rewrite the previous     content
# 
#       

# In[1]:


# Function to create a file and write to the file
def createFile(filename):
    f=open(filename,'w')
    for i in range(10):
        f.write('This is %d Line' %i)
    print("File is created and data has written")
    return
createFile('file1.txt')


# In[2]:


ls


# In[3]:


cat file1.txt


# In[5]:


def createFile(filename):
    f=open(filename,'w')
    f.write('Testing..\n')
    print("File is created and data has written")
    return
createFile('file1.txt')


# In[6]:


def appendData(filename):
    f=open(filename,'a')
    for i in range(10):
        f.write("This is %d Line\n"%i)
    print("FileCreated and Successfully data written")
    return
appendData('file2.txt')


# In[7]:


def appendData(filename):
    f=open(filename,'a')
    f.write("New Line1\n")
    f.write("New Line2\n")
    print("FileCreated and Successfully data written")
    return
appendData('file2.txt')


# In[8]:


#Function to read of the file
def readFileData(filename):
    f=open(filename,'r')
    if f.mode=='r':
        x=f.read()
        print(x)
    f.close()
    return
readFileData('file2.txt')


# In[16]:


#Function to read the File
def fileOperations(filename,mode):
    with open(filename,mode) as f:
        if f.mode=='r':
            data=f.read()
            print(data)
        elif f.mode=='a':
            f.write('Data to the File')
            print('The data successfully written')
    f.close()
    return
filename=input('Enter the file name')
mode=input('Enter the mode of the file')
fileOperations(filename,mode)


# In[21]:


#Data Analysis
#Word Count Program
def wordCount(filename,word):
    with open(filename,'r') as f:
        if f.mode=='r':
            x=f.read()
            li=x.split() # It's splits the string with whitespace
    cnt=li.count(word)
    return cnt
filename=input('Enter the file name: ')
word=input('Enter the word: ') # which word count you need
wordCount(filename,word)


# In[22]:


#character count from the given file
def charCount(filename):
    with open(filename,'r') as f:
        if f.mode=='r':
            x=f.read()
            li=list(x)
    return len(li)
filename=input('Enter the filename:')
charCount(filename)


# In[23]:


s1="Python Programming"
print(s1.split('a'))


# In[24]:


# Function to find the no of lines in the input file
# Input--filename(file2.txt)
# output--No of lines(12)
def countOfLines(filename):
    with open(filename,'r') as f:
        if f.mode=='r':
            x=f.read()
            li=x.split("\n")
    return len(li)
filename=input('Enter the filename :')
countOfLines(filename)


# In[30]:


# Function to print the upper and lower characters
def caseCount(filename):
    cntUpper = 0
    cntLower = 0
    with open(filename,'r') as f:
        if f.mode == 'r':
            x=f.read()
            li=list(x)
    for i in li:
        if i.isupper():
            cntUpper+=1 #cntUpper=cntUpper+1
        elif i.islower():
            cntLower+=1 #cntLower=cntLower+1
    output='Upper Case={0},Lower Case={1}'.format(cntUpper,cntLower)
    return output
filename=input('Enter the filename :')
caseCount(filename)


#  ### math,random,os
# - os package it contains the certains methods which works with OS
# 

# In[31]:


ls


# In[39]:


cd Desktop/PythonProg/Git


# In[46]:


cd gitam-june-2019


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




