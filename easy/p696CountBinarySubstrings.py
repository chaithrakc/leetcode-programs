# Algorithm:
# 1. Form the group - convert the string s into an array groups that represents the length of same-character
# contiguous blocks within the string.
# For example, if s = "110001111000000", then groups = [2, 3,4, 6]
# 2. count the number of valid binary strings between groups[i] and groups[i+1]
# For example, groups[i] = 2, groups[i+1] = 3, then it represents either "00111" or "11000".
# min(groups[i], groups[i+1]) is counted as valid

class SolutionCountBinarySubstrings:
    def count_binary_substrings(self, binary_str: str) -> int:
        groups = [1]  # first element always belongs to its own group
        for str_index in range(1, len(binary_str)):
            if binary_str[str_index-1] != binary_str[str_index]:
                groups.append(1)
            else:
                groups[-1] += 1

        total_subgroups = 0
        for grp_index in range(1, len(groups)):
            total_subgroups += min(groups[grp_index-1], groups[grp_index])
        return total_subgroups
