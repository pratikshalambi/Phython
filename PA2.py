#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.	Write a Python program to convert kilometers to miles?
a=input("Give the Kilometers you want to convert to miles: ")
a=float(a)
m=a*0.6214
print("miles: ",m)


# In[3]:


#2.	Write a Python program to convert Celsius to Fahrenheit?
#(°C x 9/5) + 32 =°F
a=input("Give the celsius :")
a=float(a)
f=(a*(9/5))+32
print("Fahrenheit",f,"")


# In[4]:


#3.	Write a Python program to display calendar?
import calendar
y=input("Give the year for which you want the calender to be displayed: ")
y=int(y)
print(calendar.calendar(y))      


# In[5]:


#4.Write a Python program to solve quadratic equation?
# import complex math module
#x = −b ± √(b2 − 4ac) 2a
import cmath

a = input("a:")
b = input("b:")
c = input("c:")

a=int(a)
b=int(b)
c=int(c)

# calculating the discriminant
dis = (b*b) - (4 * a*c)

# find two results
ans1 = (-b-cmath.sqrt(dis))/(2 * a)
ans2 = (-b + cmath.sqrt(dis))/(2 * a)

# printing the results
print('The roots are')
print(ans1)
print(ans2)


# In[6]:


#5 Write a Python program to swap two variables without temp variable?
a=input("Give first number: ")
b=input("Give Second number: ")
a=int(a)
b=int(b)
a,b=b,a
print("First number after swaping:",a)
print("First number after swaping:",b)

