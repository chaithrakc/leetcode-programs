"""
The sorted() method sorts iterable data such as lists, tuples, and dictionaries. But it sorts by key only.

"""
footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

# sorting the dictionaries based on the values in descending order

# Return a new list containing all items from the iterable
sorted_dict = sorted(footballers_goals.items(), key=lambda x: x[1], reverse=True)
print(sorted_dict)

