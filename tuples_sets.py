# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# simple tuple
fruit_tuple = ('Apple','Orange','Mango') 

#using constructor

# fruit_tuple = tuple(('Apple','Orange','Mango'))
# get simple value
# print(fruit_tuple[1])

# Tuples with one value should have trailing comma
fruit_tuple_2 = ('Apple',)

# delete tuple
del fruit_tuple_2
# get length of tuple
# print(len(fruit_tuple))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# create a set
fruit_set = {'Apple', 'Orange','Mango'}

# check if in set
print('Apple' in fruit_set)

# add to a set
fruit_set.add('Grape')

# remove from set
fruit_set.remove('Grape')


# clear set
fruit_set.clear()

# delete set
del fruit_set

print(fruit_set)