# https://techbeamers.com/find-palindromes-anagrams-list-strings-python/

"""
Program:
 Python program to find palindromes in a list of strings using Python lambda.

"""
from typing import List

def get_palindromes(input_strings:List[str]):
    palindromes_slicing = list(filter(lambda the_str: the_str.lower() == the_str.lower()[::-1], input_strings))
    palindromes_reverse_func = list(filter(lambda the_str: the_str.lower() == "".join(reversed(the_str.lower())),
                                           input_strings))

    print("*******************")
    print('Palindrome with string slicing = {}'.format(palindromes_slicing))
    print('Palindromes with reverse function= {}'.format(palindromes_reverse_func))
    print("*******************\n")

if __name__ == '__main__':
    input_string_list = ['Python', 'Radar', 'CSharp', 'Madam', 'Programmer', 'Noon', 'Refer', 'Php', 'Go']
    get_palindromes(input_string_list)

