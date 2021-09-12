import collections


class SolutionOriginalDigits:
    def original_digits(self, s: str) -> str:
        count_letters = collections.Counter(s)  # frequency of letters

        # frequency of digits
        count_digits = dict()

        count_digits['0'] = count_letters['z']
        count_digits['2'] = count_letters['w']
        count_digits['6'] = count_letters['x']
        count_digits['8'] = count_letters['g']
        count_digits['4'] = count_letters['u']
        count_digits['5'] = count_letters['f'] - count_digits['4']
        count_digits['7'] = count_letters['s'] - count_digits['6']
        count_digits['3'] = count_letters['h'] - count_digits['8']
        count_digits['1'] = count_letters['o'] - count_digits['0'] - count_digits['2'] - count_digits['4']
        count_digits['9'] = count_letters['i'] - count_digits['5'] - count_digits['6'] - count_digits['8']

        original_digits = [key * count_digits[key] for key in sorted(count_digits.keys())]
        return ''.join(original_digits)
