#Example: sum of digits (state is n)
def sum_digits(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

n = int(input("Enter number: "))
print("Sum of digits:", sum_digits(n))

#Recursion with extra parameters (accumulator)

def sum_digits_acc(n: int, acc: int = 0) -> int:
    n = abs(n)
    if n == 0:
        return acc
    return sum_digits_acc(n // 10, acc + (n % 10))

#factorial with accumulator

def factorial_acc(n: int, acc: int = 1) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return acc
    return factorial_acc(n - 1, acc * n)


