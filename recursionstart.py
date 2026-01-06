#infinite recursion

def f(n):
    if n == 0:
        return 0
    return f(n + 1)  # moves away from 0
f(5)


#non finite recursion

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
countdown(5)



#call stack in recursion
#factorial example


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter n: "))
print("Factorial:", factorial(n))