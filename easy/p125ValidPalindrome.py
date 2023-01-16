class SolutionValidPalindrome:
    @staticmethod
    def isPalindrome(s: str) -> bool:
        input_str = list()

        # removing non-alphabetically characters and applying lowercase transformation
        for char in s:
            if str.isalpha(char):
                input_str.append(char.lower())

        return input_str == input_str[::-1]
