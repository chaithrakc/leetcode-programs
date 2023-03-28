# Check if Python List Contains Elements of Another List - all(), any(), set intersection() methods

"""
In the sample below, we are using two lists having overlapping values. One of these is the big one which holds all
the elements of the second one.

List1 – This list contains all or some of the elements of another.
List2 – It is a subset of the first one.
Now, we’ve to programmatically prove that the List1 contains the elements of the List2.

"""

# all() method
list1 = ['python', 'javascript', 'csharp', 'go', 'c', 'c++']
list2 = ['csharp', 'go', 'python']

check = all(item in list1 for item in list2)
if check is True:
    print(f"The list {list1} contains all elements of the list {list2}")
else:
    print("No, List1 doesn't have all elements of the List2")

# any() method: to check if the list contains any elements of another one.
list1 = ['python', 'javascript', 'csharp', 'go', 'c', 'c++']
list2 = ['swift', 'php', 'python']

check = any(item in list1 for item in list2)

if check is True:
    print("The list {} contains some elements of the list {}".format(list1, list2))
else :
    print("No, List1 doesn't have any elements of the List2.")


# set() method
set1 = set(list1)
set2 = set(list2)
common_elems = set1.intersection(set2) # returns set of intersecting elements
print(common_elems)