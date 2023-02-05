# https://techbeamers.com/python-for-loop-example/

#Prepare a list
elements = ["Python", 3, 8, "CSharp", "PHP"]

# traverse a list from the end
for ele in reversed(elements):
    print(ele)

# reversing the list using slice operator
for ele in elements[::-1]:
    print(ele)


# loop to enumerate the list with index
for index, data in enumerate(elements):
    print('index {} - {}'.format(index, data))

# traversing a sorted list - it required all the elements of same datatype for comparing the elements in order to sort
elements = [11, 23, 43, 17, 32]
for ele in sorted(elements):
    print(ele)

# Iterate multiple lists with for loop in Python
countries = [ 'USA', 'Germany', 'France', 'India', 'China' ]
capitals = [ 'Washington, D.C.', 'Berlin', 'Paris', 'Delhi', 'Beijing']
population = [ 702000, 3570000, 2140000, 19000000, 21500000]

for country, capital, size in zip(countries, capitals, population):
    print('{0:<10} {1:<20} {2:<5}'.format(country, capital, size)) # left justified, number of characters




