#!/usr/bin/env python
# coding: utf-8

# In[63]:


#1 Write a Python Program to Find the Factorial of a Number?
a=int(input("Give a number: "))
t=1      
for i in range(1,a+1):
    t=t*i
print("The factorial of",a,"is: ",t)    


# In[185]:


#2 Write a Python Program to Display the multiplication Table?
a=int(input("give a number for which you want multiplication table displayed: "))

for i in range(1,11):
    z=a*i
    print(a,"*",i,"=",z)


# In[181]:


#3 Write a Python Program to Print the Fibonacci sequence?
print("Fibonacci sequence")
f=0
print(f)
s=1
print(s)
z=0
for i in range(1,10):
    z=f+s
    print(z)
    f=s
    s=z


# In[161]:


#4 Write a Python Program to Check Armstrong Number?
a=input("Give a number: ")
b=int(a)
k=b
g=b
e=0
for i in range(len(str(a))):
    b=g
    b=b%10
    g=int(g/10)
    e=e+b**(len(str(a)))
#print("final number",e)
#print("first number",k)
if (e==k):
    print("This number is a armstrong number")
else:
    print("This number is not a armstrong number")


# In[159]:


#5 Write a Python Program to Find Armstrong Number in an Interval?
e=0
print("Armstrong Numbers between the Range ")
for i in range(1,2000): 
    k=i
    y=str(k)
    z=len(y)
    b=i
    g=i
    e=0
    #print("iteration",k)
    for j in range(z):
        b=g
        b=b%10
        g=int(g/10)
        e=e+b**z
        #print("Answer",e)
    if (e==k):
        print(k)
        #else:
            #print("The number is not a amstrong number")


# In[69]:


#6 Write a Python Program to Find the Sum of Natural Numbers?
a=int(input("Give a number "))
if a<0:
    print("not a natural number")
else:
    s=0
    for i in range(1,a+1):
        s=s+i
    print("The sum of natural number is",s)    

