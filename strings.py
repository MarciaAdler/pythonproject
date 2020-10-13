# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Brad'
age = 37

# concatenate
# print('Hello I am ' + name + ' and I am ' + str(age))


# String Formatting

# arguments by position
# print('{},{},{}'.format('a','b','c'))
# print('{1},{2},{0}'.format('a','b','c'))

# arguments by name
# print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-strings (only in 3.6+)
# print(f'My name is {name} and I am {age}')

# String Methods
s = 'hello there world'

# Capitalize first letter
print(s.capitalize())

# Make all uppercase
print(s.upper())

# swap case
print(s.swapcase())

# get length
print(len(s))

# replace
print(s.replace('world', 'everyone'))

# count 
sub = "h"
print(s.count(sub))