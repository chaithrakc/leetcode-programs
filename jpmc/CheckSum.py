"""
https://stackoverflow.com/questions/26642051/credit-card-number-validity-with-luhns-algorithm-java#:~:text=Double%20every%20second%20digit%20from,1%20%2B%207%20%2B%208%20%3D%2037

Credit card numbers are generated following this validity check, commonly known as the Luhn check or the Mod 10 check, which can be described as follows (for illustration, consider the card number 4388 5760 1840 2626):

Double every second digit from right to left. If doubling of a digit results in a two-digit number, add up the two digits to get a single-digit number.

Now add all single-digit numbers from Step 1: 4 + 4 + 8 + 2 + 3 + 1 + 7 + 8 = 37

Add all digits in the odd places from right to left in the card number: 6 + 6 + 0 + 8 + 0 + 7 + 8 + 3 = 38

Sum the results from Step 2 and Step 3: 37 + 38 = 75

If the result from Step 4 is divisible by 10 the card number is valid; otherwise, it is invalid. For example, the number 4388 5760 1840 2626 is invalid, but the number 4388 5760 1841 0707 is valid.
"""
class SolutionCheckSum:
    def find_check_sum(self, credit_card_num:int) -> int:
        pass

    def valid_card(self, check_sum:int) -> bool:
        pass