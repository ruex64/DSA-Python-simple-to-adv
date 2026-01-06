#Naive Fibonacci 
def fib(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)



#fibonacci with memoization

def fib(n: int, memo=None) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

n = int(input("Enter n: "))
print("Fibonacci:", fib(n))
