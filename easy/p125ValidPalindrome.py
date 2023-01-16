class SolutionValidPalindrome:
    def alphanum(self, char: str) -> bool:
        return (ord('A') <= ord(char) <= ord('Z')
                or ord('a') <= ord(char) <= ord('z')
                or ord('0') <= ord(char) <= ord('9'))

    def is_palindrome_bruteforce(self, s: str) -> bool:

        # removing non-alphabetically characters and applying lowercase transformation
        input_char_list = list()
        for char in s:
            if self.alphanum(char):
                input_char_list.append(char.lower())

        # filtered_chars = filter(lambda char: str.isalnum(char), s)
        # lowercase_filtered_chars = map(lambda char: char.lower(), filtered_chars)
        # input_char_list = list(lowercase_filtered_chars)
        reversed_char_list = input_char_list[::-1]

        return input_char_list == reversed_char_list

    # hint: every palindrome half is reverse of the other half.
    def is_palindrome_optimized(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not self.alphanum(s[i]):
                i = i + 1
            while i < j and not self.alphanum(s[j]):
                j = j - 1

            if s[i].lower() != s[j].lower():
                return False

            # updating the indices
            i, j = i + 1, j - 1

        return True

    # Time Complexity: O(n)
    # Space Complexity: O(1)
