"""
https://stackoverflow.com/questions/26642051/credit-card-number-validity-with-luhns-algorithm-java#:~:text=Double%20every%20second%20digit%20from,1%20%2B%207%20%2B%208%20%3D%2037
"""

'''
Algorithm:

CreditCard Number: 4388 5760 1840 2626

1. Double every second digit from right to left. If doubling of a digit results in a two-digit number, add up the 
two digits to get a single-digit number.

2. Now add all single-digit numbers from Step 1: 4 + 4 + 8 + 2 + 3 + 1 + 7 + 8 = 37

3. Add all digits in the odd places from right to left in the card number: 6 + 6 + 0 + 8 + 0 + 7 + 8 + 3 = 38

4. Sum the results from Step 2 and Step 3: 37 + 38 = 75

5. If the result from Step 4 is divisible by 10 the card number is valid; otherwise, it is invalid. For example, 
the number 4388 5760 1840 2626 is invalid, but the number 4388 5760 1841 0707 is valid.

'''

class SolutionCheckSum:

    # converts a string or int into list of numeric digits
    def get_digits(self, num):
        return list(map(int, str(num)))

    def find_check_sum(self, card_num) -> int:
        digits = self.get_digits(card_num) # converting string into list of digits
        doubling_digits = digits[-2::-2] # digits that needs to be doubled
        single_digits =  digits[-1::-2]
        check_sum = sum(single_digits)
        for digit in doubling_digits:
            check_sum += sum(self.get_digits(digit * 2))
        return check_sum

    def is_valid_card(self, card_num) -> bool:
        check_sum = self.find_check_sum(card_num)
        return check_sum%10 == 0

