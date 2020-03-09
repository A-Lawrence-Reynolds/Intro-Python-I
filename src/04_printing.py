"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
import math 
print("x is : %2i , y is %4.2f, z is %15s" % (x, y, z))
# x is 10, y is 2.25, z is "I like turtles!"

  
# Use the 'format' string method to print the same thing
# print("x is : {} , y is {:.2f}, z is {}".format(x, y, z)) with format 



# Finally, print the same thing using an f-string
print(f"X is {x} , Y is {y:.2f}, and Z is {z}")