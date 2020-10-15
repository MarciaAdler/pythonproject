# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John','Will','Janet','Karen']
# simple for loop
# for person in people:
#     print('current persion: ', person)

# Break out
# for person in people:
#     print('current persion: ', person)
#     if person == 'Janet':
#         break

#continue 
# for person in people:
#     if person == 'Janet':
#         continue
#     print('current person: ',person)

# Range
# for i in range(len(people)):
#     print('Current Person: ', people[i])

# for loop up to but not including second number
# for i in range(0,10):
#     print('Number ', i)

# While loops execute a set of statements as long as a condition is true.
count = 0

while count <= 10:
    print('Count: ', count)
    count += 1