n = int(input("Enter number: "))

if n < 0:
    print("Armstrong: False")
else:
    # digit count
    if n == 0:
        digits = 1
    else:
        digits = 0
        temp = n
        while temp > 0:
            digits += 1
            temp //= 10

    # armstrong sum (reverse-style)
    total = 0
    temp = n
    while temp > 0:
        last = temp % 10
        total += last ** digits
        temp //= 10

    print("Armstrong:", total == n)
