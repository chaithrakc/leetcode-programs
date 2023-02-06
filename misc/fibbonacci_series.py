# iterative approach
def fibbonacci_iterative(length:int) -> None:
    prev1 = 0
    prev2 = 1

    for _ in range(length):
        print(prev1)
        fib_val = prev1 + prev2
        prev1, prev2 = prev2, fib_val

# recursive approach
def fibonacci_recursive(length:int) -> int:
    pass

if __name__ == '__main__':
    fibbonacci_iterative(10)
