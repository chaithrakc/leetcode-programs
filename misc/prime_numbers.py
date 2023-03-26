class Solution:
    def __init__(self, the_num:int):
        self.num = the_num

    # brute force approach
    def find_prime_numbers(self) -> list:
        prime_numbers = []
        for i in range(2, self.num+1):
            if all(i % j != 0 for j in range(2, i)):
                prime_numbers.append(i)
        return prime_numbers


if __name__ == '__main__':
    solution_obj = Solution(89)
    # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]
    print(solution_obj.find_prime_numbers())
    
