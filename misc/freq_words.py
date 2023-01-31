# https://techbeamers.com/word-frequency-python-string/

"""
Program:
 Python program to count frequency of each word in a string
"""

"""
Using List to count the word frequency in a string

1. convert the string to a list. Python string has a split() method. It takes a string and some separator (actually a space in our case) to return a list.
2. need to use another list that will be empty initially to store unique values of the first list into the second one.
3. use the Python range to iterate string list having unique values that mean inside a loop.
4. In the loop, the count() function will give us the count of each unique word present in the parent string.
"""

def get_word_freq_approach1(input_string:str) -> None:
    input_str_list = input_string.split()

    unique_str_list = list()
    for the_str in input_str_list:
        if the_str not in unique_str_list:
            unique_str_list.append(the_str)

    for the_str in unique_str_list:
        print('Word Frequency [{}]:{}'.format(the_str, input_str_list.count(the_str)))

"""
Using Python set method to get the word frequency
"""
def get_word_freq_approach2(input_string:str) -> None:
    input_str_list = input_string.split()
    unique_strings = set(input_str_list)
    for entry in unique_strings:
        print('Word Frequency [{}]:{}'.format(entry, input_str_list.count(entry)))

def driver():
   input_string ='python csharp javascript php python javascript csharp python csharp php'
   print('************************ Approach 1 ******************************')
   get_word_freq_approach1(input_string)
   print('\n************************ Approach 2 ******************************')
   get_word_freq_approach2(input_string)

if __name__=="__main__":
   driver()