class SolutionValidPalindrome:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        input_char_list = list()

        # removing non-alphabetically characters and applying lowercase transformation
        for char in s:
            if str.isalpha(char):
                input_char_list.append(char.lower())

        reversed_char_list = input_char_list[::-1]

        return input_char_list == reversed_char_list
