#!/usr/bin/env python
# coding: utf-8

# In[56]:


#1 Write a Python Program to Check if a Number is Positive, Negative or Zero?
a=input("Give a number: ")
a=int(a)
if(a<0):   
    print("The number is Negetive")
elif(a>0):
    print("The number is Positive")
else:
    print("The number is zero") 


# In[45]:


#2 Write a Python Program to Check if a Number is Odd or Even?
a=input("Give a number: ")
a=int(a)
if(a%2==0):
    print("The number is even")
else:
    print("The number is odd")


# In[77]:


#3 Write a Python Program to Check Leap Year?
n=int(input("give the year you want to check:"))
if(n%4==0): 
    if(n%100==0):
        if(n%400==0):
            print("leap year")
        else:
            print("Not a leap year")
    else:
        print("leap year")      
else:
         print("Not a leap year")    


# In[24]:


#4 Write a Python Program to Check Prime Number?
import math

def cp(n):
    temp=int(math.sqrt(n))+1
    for i in range(2,temp):
        if(n%i==0):
            return("its not a prime number") 
    return("its a prime number") 

n=int(input("give a number"))
if(n==2):
    print("its a prime number")
else:
    print(cp(n))


# In[76]:


#5 Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

import math

def cp(n):
    temp=int(math.sqrt(n))+1
    for i in range(2,temp):
        if(n%i==0):
            return(False)
            #break
        else:    
            return(True) 
m=[2]
for i in range(1,10000):
    a=cp(i)
    if(a==True):
        m.append(i)
        
print(m)


# In[ ]:




