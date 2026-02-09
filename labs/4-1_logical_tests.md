# BFOR 206 Lab 4-1: Logical Tests

## Task Description

Write a script that takes two numbers and adds them together.

The script should use an if statement to check that there are two arguments.
If there are exactly two arguments, add them together and show the result.
If there are greater/fewer than two arguments, let the user know and
exit the script without trying to add the numbers together.

## Test Cases

```shell
######## Normal scenario ##########

# Input: 
python logic_lab.py 20 21
# Output: 
sum = 41

######## Abnormal scenarios ##########

# Input:  
python logic_lab.py 9
# Output: 
Error! 1 argument(s), need exactly two.

# Input 
python logic_lab.py 1 2 3
# Output: 
Error! 3 argument(s), need exactly two.
```

## Submission instructions

**Scripts that output Python errors will not be accepted!**

When you are finished, show the instructor:

1. Your code.
2. The correct output as defined in the test
   cases.
