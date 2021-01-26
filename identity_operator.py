""" identity operator
1)is
2)is not

"""

# returns True if the both variables are the same object

# example

x = ['hello', 'world']
y = ['hello', 'world']
z = x
print( x is y) # returns False because x is not the same object as y, even if they have the same content
print(z is x)
print(x is  z)

# is not :- return True if both variables are not same object

x = ['hello', 'world']
y = ['hello', 'world']
z = x
print(z is not x)
print( x is not y)



