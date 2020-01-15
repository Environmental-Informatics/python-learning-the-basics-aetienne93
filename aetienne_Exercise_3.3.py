
#Date Created: Monday January 13th, 2020
#Creator: Aaron Etienne
#Description: Excercise 3.3- creating a 4x4 grid
# coding: utf-8

# In[1]:
##Import necessary functions 

from __future__ import print_function, division


# In[2]:
##Define commands for two and four repeat


def do_cmd_twice(f):
    f()
    f()

def do_cmd_four(f):
    do_cmd_twice(f)
    do_cmd_twice(f)


# In[3]:
## Define commands for beam and post structures 

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')


# In[4]:
## Define commands for multiple beams and posts structures 

def print_mult_beams():
    do_cmd_twice(print_beam)
    print('+')

def print_mult_posts():
    do_cmd_twice(print_post)
    print('|')


# In[5]:
##Define commands for creating row and grid structures 

def print_row():
    print_mult_beams()
    do_cmd_four(print_mult_posts)

def print_grid():
    do_cmd_twice(print_row)
    print_mult_beams()


# In[6]:
## Create the 4 x 4 grid and compare for accuracy 

print_grid()

