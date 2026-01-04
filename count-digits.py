num = int(input("Enter a number: "))

# If you want to count digits for negative numbers too
num = abs(num)

# Edge case: 0 has 1 digit
if num == 0:
    count = 1
else:
    count = 0
    while num > 0:
        last = num % 10
        count += 1
        num = num // 10  # integer division

print("Digits:", count)
