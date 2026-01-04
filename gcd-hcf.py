a = int(input("Enter a: "))
b = int(input("Enter b: "))

a = abs(a)
b = abs(b)

# Define gcd(0,0) as 0 for practicality
while b != 0:
    a, b = b, a % b

print("GCD/HCF:", a)
