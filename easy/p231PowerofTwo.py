import math


class SolutionPowersOfTwo:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        the_val = math.log10(n)/math.log10(2) # this should return an integer type to be considered as log2(x)
        return math.ceil(the_val) == math.floor(the_val)