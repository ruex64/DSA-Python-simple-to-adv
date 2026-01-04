n = int(input("Enter number: "))

# Define behavior: negative numbers are not palindromes
if n < 0:
    print("Palindrome: False")
else:
    num = n
    rev = 0

    while num > 0:
        last = num % 10
        rev = rev * 10 + last
        num //= 10

    # handles n == 0 correctly because rev stays 0
    print("Palindrome:", n == rev)
