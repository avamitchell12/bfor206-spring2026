"""
This script is going to show 
different types of variables 
and data types. It will also
show how to read command-line 
arguments.
"""
# import external libraries
import sys

# view arguments with sys
print(f'The arguments are {sys.argv}')

# show indexing
idx = 2
# debug statement to show idx and the number of args
print(f'idx = {idx}; sys.argv length = {len(sys.argv)}')

# show a specific argument
print(f'Element {idx} is {sys.argv[idx]}')
# print('Element', idx, 'is', sys.argv[idx]) # uglier but equivalent


# make a few variables
x = int(sys.argv[1]) # int() forces the sting to an integer
y = 25

# show the type of the variables
print(f'x is type {type(x)}; y is type {type(y)}')

# print(x, y) # minimal information!
print(f'x = {x}, y = {y}')

# do some addition
z = x + y

print(f'z = {z}')