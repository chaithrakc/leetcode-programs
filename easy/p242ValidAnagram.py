class SolutionValidAnagram:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_table = dict()
        for char in s:
            count_table[char] = count_table.get(char, 0) + 1

        for char in t:
            count_table[char] = count_table.get(char, 0) - 1
            if count_table[char] < 0:
                return False

        return True

    # Time Complexity: O(n)
    # Space Complexity: O(n)

    # one line pythonic code solutions
    # return sorted(s) == sorted(t)
    # return Counter(s) == Counter(t)
