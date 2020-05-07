# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(num):
    return num % 2== 0

print(is_even(2))
# Read a number from the keyboard
num = int(input("Enter a number: "))
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
if (num % 2)==0:
    print(num,"is Even")
else:
    print(num, "is Odd")
# YOUR CODE HERE

