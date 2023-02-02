# https://techbeamers.com/python-for-loop-example/

#Prepare a list
elements = ["Python", 3, 8, "CSharp", "PHP"]

# traverse a list from the end
for ele in reversed(elements):
    print(ele)

# reversing the list using slice operator
for ele in elements[::-1]:
    print(ele)