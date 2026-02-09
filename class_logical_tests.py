"""
This script will demonstrate logical tests
in Python.

A logical test is a statement that is either
True or False. A variable that stores True/False
is called a "boolean". 
"""
# imports
import sys


# a basic if statement that is always True
if True:
    print("This will always be True")
elif True:
    print("This will never run because the if is true.")

# check an argument 
a = int(sys.argv[1])    # force the argument to an integer type
print(f'The value of a = {a}.')

# use an if to check it
a_equals_10 = False
if a > 10:
    print("The value of a is greater than 10.")
elif a < 10:
    print("The value of a is less than 10.")
else:
    print("The value of a must be 10.")
    a_equals_10 = True

# a_equals_10 = (a == 10) # doesn't even need the if!
print(f'Is a == 10?: {a_equals_10}')

# the 'not' keyword reverses True/False evaluation
if not a > 10:
    print("a is less than or equal to 10.")