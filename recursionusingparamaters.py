def sum_digits(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)
