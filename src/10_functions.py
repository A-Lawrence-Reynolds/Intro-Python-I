# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(number):
   return number % 2==0
     
print(is_even(32))

# Read a number from the keyboard
# num = input("Enter a number: ")
# num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
# this works in thew pipenv but not in the terminal not sure why 
num = int(input("enter any num: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
