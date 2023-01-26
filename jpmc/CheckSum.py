"""
https://stackoverflow.com/questions/26642051/credit-card-number-validity-with-luhns-algorithm-java#:~:text=Double%20every%20second%20digit%20from,1%20%2B%207%20%2B%208%20%3D%2037
"""

class SolutionCheckSum:
    def get_digits(self, num):
        return [int(digit) for digit in str(num)]

    def find_check_sum(self, card_num) -> int:
        digits = self.get_digits(card_num) # converting string into list of digits
        doubling_digits = digits[-2::-2] # digits that needs to be doubled
        single_digits =  digits[-1::-2]
        check_sum = sum(single_digits)
        for digit in doubling_digits:
            check_sum += sum(self.get_digits(digit * 2))
        return check_sum

    def valid_card(self, card_num) -> bool:
        check_sum = self.find_check_sum(card_num)
        return True if check_sum%10 == 0 else False

