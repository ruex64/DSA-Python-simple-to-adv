num = int(input("Enter number: "))

if num == 0:
    print("0 has infinitely many factors (every non-zero integer divides 0).")
else:
    n = abs(num)
    factors = []

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            factors.append(i)

    factors.append(n)  # include the number itself
    print("Factors:", factors)
