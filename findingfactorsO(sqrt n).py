num = int(input("Enter number: "))

if num == 0:
    print("0 has infinitely many factors (every non-zero integer divides 0).")
else:
    n = abs(num)
    small = []
    large = []

    i = 1
    while i * i <= n:
        if n % i == 0:
            small.append(i)
            if i != n // i:
                large.append(n // i)
        i += 1

    factors = small + large[::-1]
    print("Factors:", factors)
