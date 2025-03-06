"""
============== OPERATORS ==============
Following are some common operators in python:
1. Arithmetic operators: +, -, *, / etc.
2. Assignment operators: =, +=, -= etc.
3. Comparison operators: ==, >, >=, <, != etc.
4. Logical operators: and, or, not.
"""

""" How it's Work:
7 + 4 = 11

Here: 
"7" and "4" is a operands.
"+" is a Arithmetic operators and "=" is Assignment operators.
"11" is a Result.
"""

# Arithmetic Operators
print("========== RESULT OF ARITHMETIC OPERATORS ==========")
a = 5
b = 5
print(a + b)

# Assignment Operators
print("========== RESULT OF ASSIGNMENT OPERATORS ==========")
c = 10 - 5 # It's Assign 10 - 5 in c 
print(c)

d = 9
d += 3 # Increment the value of d by 3 and then assign it to d.
print(d) 

# Comparison Operators (Comparison operators always return boolean value "True / False")
print("========== RESULT OF COMPARISON OPERATORS ==========")
e = 5 < 4
print(e)

f = 9 > 8
print(f)

# Logical operators
print("========== RESULT OF LOGICAL OPERATORS ==========")

# Truth Table of "OR"
print("===== Truth Table of 'OR' =====")
print("True or False is: ", True or False)
print("True or True is: ", True or True)
print("False or True is: ", False or True)
print("False or False is: ", False or False)

# Truth Table of "AND"
print("===== Truth Table of 'OR' =====")
print("True and False is: ", True and False)
print("True and True is: ", True and True)
print("False and True is: ", False and True)
print("False and False is: ", False and False)

# Example of "NOT" Operator 
print("===== Example of 'NOT' Operator =====")
print(not(False))
