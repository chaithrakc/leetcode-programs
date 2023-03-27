"""
Program:
 Python program to find anagrams in a list of strings

An anagram is a word or phrase constituted by ordering the characters of a different word or phrase.
"""
from typing import List
from collections import Counter


def get_anagrams_counter(input_strings_list: List[str], test_string: str) -> None:
    test_counter = Counter(test_string.lower())
    output_strings = list(filter(lambda x: test_counter == Counter(x.lower()), input_strings_list))

    print('\n *********************** Using lambda and Counter object ***********************')
    print("input_string_list = {}".format(input_strings_list))
    print("test_string = {}".format(test_string))
    print("out_string_list = {}".format(output_strings))


def get_anagrams(input_strings_list: List[str], test_string: str) -> None:
    # lower case transformation
    output_strings = list()

    counter_table_teststr = dict()
    for char in test_string.lower():
        counter_table_teststr[char] = counter_table_teststr.get(char, 0) + 1

    for the_str in input_strings_list:
        if len(the_str) != len(test_string):
            continue
        counter_table_input_str = dict()
        for char in the_str.lower():
            counter_table_input_str[char] = counter_table_input_str.get(char, 0) + 1

        # comparing the two dictionaries with equal operator
        if counter_table_teststr == counter_table_input_str:
            output_strings.append(the_str)

    print('\n *********************** Using dictionaries  ***********************')
    print("input_string_list = {}".format(input_strings_list))
    print("test_string = {}".format(test_string))
    print("out_string_list = {}".format(output_strings))


if __name__ == '__main__':
    input_string_list = ['Python', 'Program', 'Machine', 'yPtnoh', 'Learning']
    test_string = "ntoyPh"
    get_anagrams(input_string_list, test_string)
    get_anagrams_counter(input_string_list, test_string)

