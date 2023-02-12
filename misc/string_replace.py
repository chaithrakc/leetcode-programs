# https://techbeamers.com/replace-occurrences-string-python/

"""
Python's String Replace Function

python_string.replace(old_str, new_str, count)

Parameters:

 old_str => Old string to be replaced
 new_str => New string used for substitution
 count => Replacement counter

Returns:

 Returns a new copy of the string.

"""

if __name__ == '__main__':
    # task1: replace "easy" with "simple"
    original_str = 'Python Programming language is easy to learn and easy to code.'
    print(original_str.replace('easy', 'simple'))

    #task2 :  replace period character with exclamation in the original string.
    print(original_str.replace('.', '!'))

    #task3: replace 2 occurrences
    original_str = 'Python Programming language, Python Programmer, Python Unit Testing.'
    new_str = original_str.replace('Python', 'CSharp', 2)
    print(new_str)




