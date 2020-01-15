#Date Created: Monday January 13th, 2020
#Creator: Aaron Etienne
#Description: Excercise 3.2- do command twice 
# coding: utf-8

# In[1]:
## Import the necessary functions 

from __future__ import print_function, division


# In[2]:
## define the function for calling an argument 2 times (needs function and argument block) 

def do_twice(func, arg):
   
    func(arg)
    func(arg)


# In[3]:
## define printing of do_twice argument

def print_twice(arg):
  
    print(arg)
    print(arg)


# In[4]:
##Put it together (call print twice within do twice function) 

do_twice(print_twice, 'spam')
print('')


