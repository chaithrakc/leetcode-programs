# Conversion of a mixed list to a string using join()

"""

https://techbeamers.com/python-convert-list-string/

Let’s assume that we have got a list of some numbers and strings.
Since it is a combination of different objects, so we need to handle it a little differently.

It is not possible to use the join() function on this list.
We first have to convert each element to a string to form a new one, and then only we can call join() method.

"""

if __name__ == '__main__':
    sourceList = ["I", "got", 60, "in", "Science", 70, "in", "English", ", and", 66, "in", "Maths"]
    string_list = ' '.join([str(item) for item in sourceList])
    print(string_list)

    # Get a comma-separated string from a list of numbers
    numList = [20,213,4587,7869]
    comma_delimited = str(numList).strip('[]')
    print(comma_delimited)

    # Alternatively, we can use map() function to convert the items in the list to a string. After that,
    # we can join them as below:
    comma_delimited = ','.join(map(str, numList))
    print(comma_delimited)

    # We can even use the new line character (‘\n’) as a separator.
    newline_str = '\n'.join(map(str, numList))
    print(newline_str)



