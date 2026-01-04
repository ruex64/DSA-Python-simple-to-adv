# DSA in Python - Notes & Documentation

A comprehensive guide to solving Data Structures and Algorithms problems in Python, focusing on **Digit Manipulation** patterns.

---

## Table of Contents

1. [Count Digits](#1-count-digits)
2. [Reverse a Number](#2-reverse-a-number)
3. [Check Palindrome](#3-check-palindrome)
4. [Armstrong Number](#4-armstrong-number)
5. [Sum of Digits](#5-sum-of-digits)
6. [GCD / HCF](#6-gcd--hcf-greatest-common-divisor)

---

## Pattern: Digit Manipulation

This pattern involves extracting and manipulating individual digits of a number using:
- **Modulo operator (`%`)** → to get the last digit
- **Integer division (`//`)** → to remove the last digit

### Core Concept

```
For any number n:
  last_digit = n % 10      # gives remainder when divided by 10
  remaining  = n // 10     # removes the last digit
```

---

## 1. Count Digits

**Problem:** Given a number, count how many digits it has.

**File:** `count-digits.py`

### Approach

Extract digits one by one from the right side until the number becomes 0. Each extraction counts as one digit.

### Pseudocode

```
FUNCTION countDigits(num):
    num = |num|                    # Handle negative numbers
    
    IF num == 0:
        RETURN 1                   # Edge case: 0 has 1 digit
    
    count = 0
    WHILE num > 0:
        last = num MOD 10          # Extract last digit (optional, for clarity)
        count = count + 1          # Increment counter
        num = num DIV 10           # Remove last digit
    
    RETURN count
```

### Code Explanation

```python
num = int(input("Enter a number: "))

# If you want to count digits for negative numbers too
num = abs(num)
```
- Take input and convert to integer
- Use `abs()` to handle negative numbers (e.g., -123 has 3 digits, not 4)

```python
# Edge case: 0 has 1 digit
if num == 0:
    count = 1
```
- Special handling: The while loop won't execute for 0, but 0 has 1 digit

```python
else:
    count = 0
    while num > 0:
        last = num % 10        # Get the last digit
        count += 1             # Count this digit
        num = num // 10        # Remove the last digit
```
- **Loop condition:** Continue while there are digits left
- **`num % 10`:** Extracts the last digit (optional here, just for clarity)
- **`count += 1`:** Increment the digit counter
- **`num // 10`:** Integer division removes the last digit

### Dry Run

| Step | num | last (num % 10) | count | num // 10 |
|------|-----|-----------------|-------|-----------|
| Input | 1234 | - | 0 | - |
| 1 | 1234 | 4 | 1 | 123 |
| 2 | 123 | 3 | 2 | 12 |
| 3 | 12 | 2 | 3 | 1 |
| 4 | 1 | 1 | 4 | 0 |
| Exit | 0 | - | **4** | - |

### Time & Space Complexity

- **Time:** O(n) where n = number of digits
- **Space:** O(1) - constant extra space

### Alternative Approaches

```python
# Method 2: Using string conversion
count = len(str(abs(num)))

# Method 3: Using logarithm (doesn't work for 0)
import math
count = math.floor(math.log10(abs(num))) + 1
```

---

## 2. Reverse a Number

**Problem:** Given a number, reverse its digits. (e.g., 1234 -> 4321)

**File:** `reverse-digits.py`

### Approach

Build the reversed number by extracting digits from the right and appending them to the result from the left.

### Pseudocode

```
FUNCTION reverseNumber(n):
    num = |n|                      # Work on absolute value
    rev = 0
    
    WHILE num > 0:
        last = num MOD 10          # Extract last digit
        rev = rev * 10 + last      # Append digit to result
        num = num DIV 10           # Remove last digit
    
    IF n == 0:
        rev = 0
    
    IF n < 0:
        rev = -rev                 # Restore negative sign
    
    RETURN rev
```

### Code Explanation

```python
n = int(input("Enter number: "))

num = abs(n)   # keep n unchanged, work on a copy (and handle negatives)
rev = 0
```
- Store original input in `n` (to check sign later)
- Work on `num` (absolute value) to simplify the logic
- `rev` will store the reversed number

```python
while num > 0:
    last = num % 10            # Extract the last digit
    rev = rev * 10 + last      # Build reversed number
    num //= 10                 # Remove the last digit
```
- **`num % 10`:** Gets the rightmost digit
- **`rev * 10 + last`:** Shifts existing digits left and adds new digit
- **`num //= 10`:** Removes the processed digit

```python
# handle input 0 explicitly (loop won't run)
if n == 0:
    rev = 0

# restore sign
if n < 0:
    rev = -rev
```
- Handle edge case for 0
- Restore the negative sign if original input was negative

### Dry Run

**Input:** 1234

| Step | num | last | rev (before) | rev * 10 + last | num //= 10 |
|------|-----|------|--------------|-----------------|------------|
| Start | 1234 | - | 0 | - | - |
| 1 | 1234 | 4 | 0 | 0 * 10 + 4 = **4** | 123 |
| 2 | 123 | 3 | 4 | 4 * 10 + 3 = **43** | 12 |
| 3 | 12 | 2 | 43 | 43 * 10 + 2 = **432** | 1 |
| 4 | 1 | 1 | 432 | 432 * 10 + 1 = **4321** | 0 |
| Exit | 0 | - | **4321** | - | - |

**Output:** 4321

### Time & Space Complexity

- **Time:** O(n) where n = number of digits
- **Space:** O(1) - constant extra space

### Edge Cases Handled

| Input | Output | Notes |
|-------|--------|-------|
| 1234 | 4321 | Normal case |
| -1234 | -4321 | Negative number |
| 0 | 0 | Zero |
| 1000 | 1 | Trailing zeros become leading (disappear) |

### Alternative Approach

```python
# Using string slicing (simpler but less efficient)
n = int(input("Enter number: "))
sign = -1 if n < 0 else 1
rev = int(str(abs(n))[::-1]) * sign
print("Reversed:", rev)
```

---

## 3. Check Palindrome

**Problem:** Check if a number reads the same forwards and backwards. (e.g., 121, 12321)

**File:** `palindrome.py`

### Approach

Reverse the number and compare it with the original. If they match, it's a palindrome.

### Pseudocode

```
FUNCTION isPalindrome(n):
    IF n < 0:
        RETURN False               # Negative numbers aren't palindromes
    
    num = n
    rev = 0
    
    WHILE num > 0:
        last = num MOD 10
        rev = rev * 10 + last
        num = num DIV 10
    
    RETURN n == rev
```

### Code Explanation

```python
n = int(input("Enter number: "))

# Define behavior: negative numbers are not palindromes
if n < 0:
    print("Palindrome: False")
```
- Take input and convert to integer
- Negative numbers are not palindromes (e.g., -121 has a leading minus sign)

```python
else:
    num = n
    rev = 0

    while num > 0:
        last = num % 10
        rev = rev * 10 + last
        num //= 10
```
- Use `num` as a working copy, preserve original `n`
- Reverse the number using the same pattern from reverse-digits
- Build reversed number digit by digit

```python
    # handles n == 0 correctly because rev stays 0
    print("Palindrome:", n == rev)
```
- Compare original with reversed
- Edge case: 0 is a palindrome (rev stays 0, so 0 == 0)

### Dry Run

**Input:** 121

| Step | num | last | rev (before) | rev * 10 + last | num //= 10 |
|------|-----|------|--------------|-----------------|------------|
| Start | 121 | - | 0 | - | - |
| 1 | 121 | 1 | 0 | 0 * 10 + 1 = **1** | 12 |
| 2 | 12 | 2 | 1 | 1 * 10 + 2 = **12** | 1 |
| 3 | 1 | 1 | 12 | 12 * 10 + 1 = **121** | 0 |
| Exit | 0 | - | **121** | - | - |

**Comparison:** n (121) == rev (121) --> True

**Output:** Palindrome: True

### Time & Space Complexity

- **Time:** O(n) where n = number of digits
- **Space:** O(1) - constant extra space

### Key Insight

A number is a palindrome if **original == reversed**

### Edge Cases

| Input | Output | Notes |
|-------|--------|-------|
| 121 | True | Palindrome |
| 12321 | True | Odd-length palindrome |
| 123 | False | Not a palindrome (rev = 321) |
| -121 | False | Negative numbers not palindromes |
| 0 | True | Zero is a palindrome |
| 10 | False | Trailing zero (rev = 1) |

---

## 4. Armstrong Number

**Problem:** Check if a number equals the sum of its digits each raised to the power of the number of digits.

**Example:** 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 (Armstrong)

**File:** `armstrong.py`

### Approach

1. First, count the number of digits in the number
2. Then, extract each digit and add (digit ^ number_of_digits) to a running total
3. Compare the total with the original number

### Pseudocode

```
FUNCTION isArmstrong(n):
    IF n < 0:
        RETURN False               # Negative numbers aren't Armstrong
    
    digits = countDigits(n)        # Count digits first
    total = 0
    temp = n
    
    WHILE temp > 0:
        last = temp MOD 10
        total = total + (last ^ digits)
        temp = temp DIV 10
    
    RETURN total == n
```

### Code Explanation

```python
n = int(input("Enter number: "))

if n < 0:
    print("Armstrong: False")
```
- Take input and convert to integer
- Negative numbers are not Armstrong numbers

```python
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
```
- Count the number of digits using the same pattern from count-digits
- Edge case: 0 has 1 digit
- Use `temp` to preserve original `n`

```python
    # armstrong sum (reverse-style)
    total = 0
    temp = n
    while temp > 0:
        last = temp % 10
        total += last ** digits
        temp //= 10
```
- Reset `temp` to original number
- Extract each digit and raise it to the power of total digits
- Add to running total

```python
    print("Armstrong:", total == n)
```
- Compare total with original number

### Dry Run

**Input:** 153

**Step 1: Count digits**
| temp | digits |
|------|--------|
| 153 | 1 |
| 15 | 2 |
| 1 | 3 |
| 0 | 3 (exit) |

**Step 2: Calculate Armstrong sum**
| temp | last | last^3 | total |
|------|------|--------|-------|
| 153 | 3 | 27 | 27 |
| 15 | 5 | 125 | 152 |
| 1 | 1 | 1 | 153 |
| 0 | - | - | 153 (exit) |

**Comparison:** total (153) == n (153) --> True

**Output:** Armstrong: True

### Time & Space Complexity

- **Time:** O(n) where n = number of digits (two passes: count + sum)
- **Space:** O(1) - constant extra space

### Common Armstrong Numbers

| Number | Calculation |
|--------|-------------|
| 0 | 0^1 = 0 |
| 1 | 1^1 = 1 |
| 153 | 1^3 + 5^3 + 3^3 = 153 |
| 370 | 3^3 + 7^3 + 0^3 = 370 |
| 371 | 3^3 + 7^3 + 1^3 = 371 |
| 407 | 4^3 + 0^3 + 7^3 = 407 |
| 1634 | 1^4 + 6^4 + 3^4 + 4^4 = 1634 |

---

## 5. Sum of Digits

**Problem:** Find the sum of all digits in a number.

**Example:** 1234 -> 1 + 2 + 3 + 4 = 10

**File:** `sum of digits.py`

### Approach

Extract each digit from right to left and add it to a running sum.

### Pseudocode

```
FUNCTION sumOfDigits(n):
    num = |n|                      # Handle negative numbers
    sum = 0
    
    WHILE num > 0:
        last = num MOD 10          # Extract last digit
        sum = sum + last           # Add to running sum
        num = num DIV 10           # Remove last digit
    
    RETURN sum
```

### Code Explanation

```python
n = int(input("Enter number: "))

num = abs(n)
s = 0
```
- Take input and convert to integer
- Use `abs()` to handle negative numbers (sum of digits of -123 is same as 123)
- Initialize sum `s` to 0

```python
while num > 0:
    last = num % 10
    s += last
    num //= 10
```
- **`num % 10`:** Extract the rightmost digit
- **`s += last`:** Add digit to running sum
- **`num //= 10`:** Remove the processed digit

```python
# handles n == 0 correctly (sum should be 0)
print("Sum of digits:", s)
```
- Edge case: 0 has digit sum of 0 (loop doesn't run, s stays 0)

### Dry Run

**Input:** 1234

| Step | num | last | s (before) | s + last | num //= 10 |
|------|-----|------|------------|----------|------------|
| Start | 1234 | - | 0 | - | - |
| 1 | 1234 | 4 | 0 | 0 + 4 = **4** | 123 |
| 2 | 123 | 3 | 4 | 4 + 3 = **7** | 12 |
| 3 | 12 | 2 | 7 | 7 + 2 = **9** | 1 |
| 4 | 1 | 1 | 9 | 9 + 1 = **10** | 0 |
| Exit | 0 | - | **10** | - | - |

**Output:** Sum of digits: 10

### Time & Space Complexity

- **Time:** O(n) where n = number of digits
- **Space:** O(1) - constant extra space

### Edge Cases

| Input | Output | Notes |
|-------|--------|-------|
| 1234 | 10 | Normal case |
| -1234 | 10 | Negative handled with abs() |
| 0 | 0 | Zero case |
| 9999 | 36 | All 9s |
| 1000 | 1 | Trailing zeros |

### Alternative Approach

```python
# Using string conversion
n = int(input("Enter number: "))
digit_sum = sum(int(d) for d in str(abs(n)))
print("Sum of digits:", digit_sum)
```

---

## 6. GCD / HCF (Greatest Common Divisor)

**Problem:** Find the greatest common divisor (GCD) or highest common factor (HCF) of two numbers.

**Example:** GCD(48, 18) = 6

**File:** `gcd-hcf.py`

### Approach

Use **Euclidean Algorithm**: Repeatedly replace the larger number with the remainder of dividing the larger by the smaller, until one becomes 0. The other number is the GCD.

### Pseudocode

```
FUNCTION gcd(a, b):
    a = |a|                        # Handle negative numbers
    b = |b|
    
    WHILE b != 0:
        a, b = b, a MOD b          # Swap: a becomes b, b becomes remainder
    
    RETURN a
```

### Code Explanation

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a = abs(a)
b = abs(b)
```
- Take two inputs and convert to integers
- Use `abs()` to handle negative numbers (GCD is always positive)

```python
# Define gcd(0,0) as 0 for practicality
while b != 0:
    a, b = b, a % b
```
- **Euclidean Algorithm**: Keep replacing (a, b) with (b, a % b)
- Loop continues until b becomes 0
- Python's tuple swap makes this clean

```python
print("GCD/HCF:", a)
```
- When b becomes 0, a holds the GCD

### Dry Run

**Input:** a = 48, b = 18

| Step | a | b | a % b | New (a, b) |
|------|---|---|-------|------------|
| Start | 48 | 18 | - | - |
| 1 | 48 | 18 | 48 % 18 = 12 | (18, 12) |
| 2 | 18 | 12 | 18 % 12 = 6 | (12, 6) |
| 3 | 12 | 6 | 12 % 6 = 0 | (6, 0) |
| Exit | 6 | 0 | - | - |

**Output:** GCD/HCF: 6

### Why Euclidean Algorithm Works

If `d` divides both `a` and `b`, then `d` also divides `a % b` (the remainder).

So: GCD(a, b) = GCD(b, a % b)

This reduces the problem size quickly until one value becomes 0.

### Time & Space Complexity

- **Time:** O(log(min(a, b))) - very efficient
- **Space:** O(1) - constant extra space

### Edge Cases

| Input | Output | Notes |
|-------|--------|-------|
| (48, 18) | 6 | Normal case |
| (18, 48) | 6 | Order doesn't matter |
| (0, 5) | 5 | GCD(0, n) = n |
| (5, 0) | 5 | GCD(n, 0) = n |
| (0, 0) | 0 | Defined as 0 |
| (-12, 8) | 4 | Handles negatives |
| (7, 3) | 1 | Coprime numbers |

### Alternative: Finding LCM

Once you have GCD, you can find LCM (Least Common Multiple):

```python
# LCM(a, b) = (a * b) / GCD(a, b)
lcm = (a * b) // gcd_value
```

---

## Key Patterns Summary

| Operation | Code | Purpose |
|-----------|------|---------|
| Get last digit | `num % 10` | Extract rightmost digit |
| Remove last digit | `num // 10` | Reduce number |
| Build number | `rev * 10 + digit` | Append digit to right |
| Handle negative | `abs(n)` | Work with magnitude |
| Count digits | Loop until `num > 0` | Each iteration = 1 digit |

---

## Practice Problems

1. [x] Count digits in a number
2. [x] Reverse a number
3. [x] Check if number is palindrome
4. [x] Check if number is Armstrong number
5. [x] Find sum of digits
6. [x] Find GCD/HCF of two numbers

---

*Last Updated: January 4, 2026*
