n = int(input("Enter number: "))

num = abs(n)
s = 0

while num > 0:
    last = num % 10
    s += last
    num //= 10

# handles n == 0 correctly (sum should be 0)
print("Sum of digits:", s)
