# two lists - keys and values will be initialized
# combine the two lists using zip() method
#  then, convert zip object into dictionary using dict() constructor method

list_of_keys = [1,2,3,4,5]
list_of_values = [11,22,33,44,55]

the_dict = dict(zip(list_of_keys, list_of_values))
print(the_dict)