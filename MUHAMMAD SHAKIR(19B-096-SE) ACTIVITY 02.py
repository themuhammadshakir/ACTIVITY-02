#!/usr/bin/env python
# coding: utf-8

# # MUHAMMAD SHAKIR(19B-096-SE)

# # ACTIVITY NO 02

# # QUESTION NO 01

# In[136]:


import math

def Area_of_Triangle(a, b, c):
    s = (a + b + c) / 2
    Area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
    print(" The Area of a Triangle is " ,Area)
Area_of_Triangle(3,5,7)


# In[71]:


def relation(x):
    rel = {'Father':'Ali',"Mother":"Saira","Saad":"Brother","Ahsan":"Brother","Sister":"Ayesha"}
    if x == ('Father'):
         print(rel['Father'])
    elif x == ('Mother'):
         print(rel['Mother'])
    elif x == ('Brother'):
         print(rel['Brother'])
    elif x == ('Sister'):
         print(rel['Sister'])
    else:
         print("SORRY THE RELATION DOES NOT EXISTS IN YOUR FAMILY ")
relation('Son')


# # QUESTION NO 03

# In[89]:


## import math
def Area_of_Triangle(a, b, c):
    s = (a + b + c) / 2
    # calculate the area
    Area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
    print(" The Area of a Triangle is " ,Area,"m\u00b2")
Area_of_Triangle(2.25,3,5)


# # QUESTION NO 04

# In[132]:


def even_add(x,y,z,a,b,c):
    if x%2==0 | y%2==0 | z%2==0 | a%2==0 | b%2==0 | c%2==0:
        print(x+y+z+a+b+c)
    else:
        print("SORRY ALL THE NUMBERS ARE ODD")
even_add(2,2,8,4,6,8)       


# # QUESTION NO 05

# In[133]:


def sorting_list():
    x = [1,3,5,7,4,9,6]
    y = x.sort()
    print(x)
sorting_list()


# # QUESTION NO 06

# In[224]:


from math import pi
def perimeter_area(r):
# calculate the Perimeter
    perimeter = 2 * pi * r
    area = (pi*(r**2))+5
    print("PERIMETER IS ",perimeter,"m")
    print("AREA OF CIRCLE IS ",area,"m\u00b2")
perimeter_area(2) 


# # QUESTION NO 07

# In[216]:


#(A)
def vowels_consonants(x):
    if x=='a'or x=='e'or x=='i'or x=='o'or x=='u'or x=='A'or x=='E'or x=='I'or x=='O'or x=='U': 
        print(len(x))  
    return ("CONSONANTS ARE ",len(x))    
vowels_consonants("Pakistan Is A Muslim Country")                


# In[218]:


#(B)
def vowels_consonants(a):
    y=0
    for x in a:
        if x=='a'or x=='e'or x=='i'or x=='o'or x=='u'or x=='A'or x=='E'or x=='I'or x=='O'or x=='U': 
            y = y + 1
    return ("VOWELS ARE ",y)    
vowels_consonants("Pakistan Is A Muslim Country")        


# # QUESTION NO 08

# In[232]:


def rectangle(l,b):
    p=2*(l+b)
    area = (l * b) + 8
    print("THE PERIMETER OF THIS RECLANGLE IS : ",p,"m")
    print("THE AREA OF GIVEN RECTANGLE IS : ",area,"m\u00b2")
rectangle(3,6)    


# # QUESTION NO 09

# In[242]:


def string(a,b,c,x,y,z):
    even = []
    odd = []
    lst = [a,b,c,x,y,z]
    for i in lst:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print("EVEN LIST :",even)
    print("ODD LIST :",odd)
string(1,2,3,4,5,6)    


# # QUESTION NO 10

# In[248]:


def alphabet(a):
    alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
                 "N","O","P","Q","R","S","T","U","U","W","X","Y","Z"]
    for i in a:
        alphabets.remove(i)
    print("THE MISSING ALPHABETS ARE :",alphabets)   
    print("THE ALPHABETS WHICH ARE USED ARE :",a)
    for i in a:
        print(i, end=" ")
alphabet("PAK")        


# # QUESTION NO 11

# In[250]:


def continues(x):
    y = x +"ING"
    return y
continues("JUMP")


# # QUESTION NO 12

# In[253]:


from math import pi
def radius(r1,r2):
    area1 = pi * r1**2
    area2 = pi * r2**2
    if r1>r2:
        print("THE REMAINING AREA IS :",r1-r2)
    else:
        print("THE REMAINING AREA IS",r2-r1)
radius(5,8)        

