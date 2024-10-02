#God, I got a new knowledge today about how to swap value in variables
# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇

#First method: using Tuple Packing and Unpacking
"""
Tuple packing is the process of combining multiple values into a single tuple. 
A tuple is a collection of values that can hold different types of elements and is typically 
enclosed in parentheses.
"""
a,b=b,a

#Second method: using a temporary variable
#temp=a
#a=b
#b=temp

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
