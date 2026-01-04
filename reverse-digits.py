n = int(input("Enter number: "))

num = abs(n)   # keep n unchanged, work on a copy (and handle negatives)
rev = 0

while num > 0:
    last = num % 10
    rev = rev * 10 + last
    num //= 10

# handle input 0 explicitly (loop won't run)
if n == 0:
    rev = 0

# restore sign
if n < 0:
    rev = -rev

print("Reversed:", rev)
