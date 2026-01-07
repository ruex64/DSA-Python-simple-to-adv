def gcd(a: int, b: int) -> int:
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    return gcd(b, a % b)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("GCD:", gcd(a, b))
