# A List is a collection which is ordered and changeable. Allows duplicate members.

# create list
# numbers = [1,2,3,4,5]

# using constructor
numbers = list((1,2,3,4,5))

fruits = ['Appels', 'Oranges', 'Grapes', 'Pears']

# get value
print(fruits[1])

# get len
print(len(fruits))

# append to list
fruits.append('Mangos')

# insert into position
fruits.insert(2,'Strawberries')



# remove from list
fruits.remove('Grapes')

# remove from position
fruits.pop(3)

# reverse list
fruits.reverse()

# sort list
fruits.sort()

# reverse sort
fruits.sort(reverse=True)


print(fruits)