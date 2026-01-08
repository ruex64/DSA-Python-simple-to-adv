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
7. [Finding Factors](#7-finding-factors)
8. [Store Frequency in Dictionary](#8-store-frequency-in-dictionary)
9. [Recursion Basics](#9-recursion-basics)
10. [Fibonacci](#10-fibonacci)
11. [Sum of Digits (Recursion)](#11-sum-of-digits-recursion)
12. [GCD - Euclidean (Recursion)](#12-gcd---euclidean-recursion)
13. [Reverse Array (Recursion)](#13-reverse-array-recursion)

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

## 7. Finding Factors

**Problem:** Find all factors (divisors) of a given number.

**Example:** Factors of 12 = [1, 2, 3, 4, 6, 12]

**Files:** `findingfactorsO(n).py`, `findingfactorsO(sqrt n).py`

### Approach 1: Brute Force - O(n)

Check every number from 1 to n/2, then add n itself.

#### Pseudocode

```
FUNCTION findFactors_BruteForce(num):
    IF num == 0:
        PRINT "0 has infinitely many factors"
        RETURN
    
    n = |num|
    factors = []
    
    FOR i = 1 TO n/2:
        IF n MOD i == 0:
            factors.append(i)
    
    factors.append(n)              # Include the number itself
    RETURN factors
```

#### Code Explanation (O(n))

```python
num = int(input("Enter number: "))

if num == 0:
    print("0 has infinitely many factors (every non-zero integer divides 0).")
```
- Take input and handle special case: 0 is divisible by everything

```python
else:
    n = abs(num)
    factors = []

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            factors.append(i)
```
- Use `abs()` to handle negative numbers
- Loop from 1 to n/2 (no factor other than n itself can be > n/2)
- If `i` divides `n` evenly, it's a factor

```python
    factors.append(n)  # include the number itself
    print("Factors:", factors)
```
- Always add n as a factor (n divides itself)

#### Dry Run (O(n))

**Input:** 12

| i | 12 % i | Factor? | factors |
|---|--------|---------|----------|
| 1 | 0 | Yes | [1] |
| 2 | 0 | Yes | [1, 2] |
| 3 | 0 | Yes | [1, 2, 3] |
| 4 | 0 | Yes | [1, 2, 3, 4] |
| 5 | 2 | No | [1, 2, 3, 4] |
| 6 | 0 | Yes | [1, 2, 3, 4, 6] |
| End | - | Add n | [1, 2, 3, 4, 6, 12] |

**Output:** Factors: [1, 2, 3, 4, 6, 12]

#### Time & Space Complexity (O(n))

- **Time:** O(n) - loops through n/2 iterations
- **Space:** O(k) where k = number of factors

---

### Approach 2: Optimized - O(sqrt n)

Factors come in pairs. If `i` is a factor, then `n/i` is also a factor. Only need to check up to sqrt(n).

#### Key Insight

For n = 36:
- 1 x 36
- 2 x 18
- 3 x 12
- 4 x 9
- 6 x 6 (sqrt)

After sqrt(n), factors repeat in reverse!

#### Pseudocode

```
FUNCTION findFactors_Optimized(num):
    IF num == 0:
        PRINT "0 has infinitely many factors"
        RETURN
    
    n = |num|
    small = []                     # Factors <= sqrt(n)
    large = []                     # Factors > sqrt(n)
    
    i = 1
    WHILE i * i <= n:
        IF n MOD i == 0:
            small.append(i)
            IF i != n / i:         # Avoid duplicate for perfect squares
                large.append(n / i)
        i = i + 1
    
    factors = small + reverse(large)
    RETURN factors
```

#### Code Explanation (O(sqrt n))

```python
num = int(input("Enter number: "))

if num == 0:
    print("0 has infinitely many factors (every non-zero integer divides 0).")
```
- Handle the special case for 0

```python
else:
    n = abs(num)
    small = []
    large = []
```
- Two lists: `small` for factors <= sqrt(n), `large` for factors > sqrt(n)

```python
    i = 1
    while i * i <= n:
        if n % i == 0:
            small.append(i)
            if i != n // i:
                large.append(n // i)
        i += 1
```
- **`i * i <= n`:** Loop only until sqrt(n)
- If `i` is a factor, so is `n // i` (the pair)
- **`if i != n // i`:** Avoid adding sqrt(n) twice for perfect squares

```python
    factors = small + large[::-1]
    print("Factors:", factors)
```
- Reverse `large` and concatenate to get sorted order

#### Dry Run (O(sqrt n))

**Input:** 36

| i | i*i | i*i <= 36? | 36 % i | Factor? | Pair (36/i) | small | large |
|---|-----|------------|--------|---------|-------------|-------|-------|
| 1 | 1 | Yes | 0 | Yes | 36 | [1] | [36] |
| 2 | 4 | Yes | 0 | Yes | 18 | [1,2] | [36,18] |
| 3 | 9 | Yes | 0 | Yes | 12 | [1,2,3] | [36,18,12] |
| 4 | 16 | Yes | 0 | Yes | 9 | [1,2,3,4] | [36,18,12,9] |
| 5 | 25 | Yes | 1 | No | - | [1,2,3,4] | [36,18,12,9] |
| 6 | 36 | Yes | 0 | Yes | 6 (skip!) | [1,2,3,4,6] | [36,18,12,9] |
| 7 | 49 | No | - | Exit | - | - | - |

**Merge:** small + large[::-1] = [1,2,3,4,6] + [9,12,18,36] = [1,2,3,4,6,9,12,18,36]

**Output:** Factors: [1, 2, 3, 4, 6, 9, 12, 18, 36]

#### Time & Space Complexity (O(sqrt n))

- **Time:** O(sqrt n) - loops only until sqrt(n)
- **Space:** O(k) where k = number of factors

---

### Comparison

| Approach | Time | When to Use |
|----------|------|-------------|
| O(n) | O(n) | Small numbers, simpler code |
| O(sqrt n) | O(sqrt n) | Large numbers, optimized |

**Performance Example:**
- n = 1,000,000
- O(n): ~500,000 iterations
- O(sqrt n): ~1,000 iterations (500x faster!)

---

## 8. Store Frequency in Dictionary

**Problem:** Count the frequency (occurrences) of each element in a list/array and store it in a dictionary.

**Example:** [1, 2, 2, 3, 1, 2] -> {1: 2, 2: 3, 3: 1}

**File:** `storeFrequencyinDictionary.py`

### Approach 1: Using if-else

Check if element exists in dictionary, increment if yes, otherwise initialize to 1.

#### Pseudocode

```
FUNCTION countFrequency_IfElse(data):
    freq = {}
    
    FOR each x IN data:
        IF x IN freq:
            freq[x] = freq[x] + 1
        ELSE:
            freq[x] = 1
    
    RETURN freq
```

#### Code Explanation

```python
data = [1, 2, 2, 3, 1, 2]
freq = {}
```
- Input list/array of elements
- Initialize empty dictionary to store frequencies

```python
for x in data:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
```
- Loop through each element in data
- **`if x in freq`:** Check if key already exists
- If exists: increment the count
- If not: initialize count to 1

```python
print(freq)  # {1: 2, 2: 3, 3: 1}
```
- Output: dictionary with element as key, frequency as value

#### Dry Run

**Input:** [1, 2, 2, 3, 1, 2]

| Step | x | x in freq? | Action | freq |
|------|---|------------|--------|------|
| 1 | 1 | No | freq[1] = 1 | {1: 1} |
| 2 | 2 | No | freq[2] = 1 | {1: 1, 2: 1} |
| 3 | 2 | Yes | freq[2] += 1 | {1: 1, 2: 2} |
| 4 | 3 | No | freq[3] = 1 | {1: 1, 2: 2, 3: 1} |
| 5 | 1 | Yes | freq[1] += 1 | {1: 2, 2: 2, 3: 1} |
| 6 | 2 | Yes | freq[2] += 1 | {1: 2, 2: 3, 3: 1} |

**Output:** {1: 2, 2: 3, 3: 1}

---

### Approach 2: Using dict.get()

Use the `get()` method which returns a default value if key doesn't exist.

#### Pseudocode

```
FUNCTION countFrequency_Get(data):
    freq = {}
    
    FOR each x IN data:
        freq[x] = freq.get(x, 0) + 1
    
    RETURN freq
```

#### Code Explanation

```python
data = [1, 2, 2, 3, 1, 2]
freq = {}
```
- Same setup as before

```python
for x in data:
    freq[x] = freq.get(x, 0) + 1
```
- **`freq.get(x, 0)`:** Returns freq[x] if exists, otherwise returns 0
- Add 1 to the returned value and assign back
- Single line replaces the entire if-else block!

```python
print(freq)
```
- Same output: {1: 2, 2: 3, 3: 1}

#### How dict.get() Works

| Expression | x exists? | Returns |
|------------|-----------|----------|
| freq.get(x, 0) | Yes | freq[x] (current count) |
| freq.get(x, 0) | No | 0 (default value) |

#### Dry Run

**Input:** [1, 2, 2, 3, 1, 2]

| Step | x | freq.get(x, 0) | + 1 | freq |
|------|---|----------------|-----|------|
| 1 | 1 | 0 (not found) | 1 | {1: 1} |
| 2 | 2 | 0 (not found) | 1 | {1: 1, 2: 1} |
| 3 | 2 | 1 | 2 | {1: 1, 2: 2} |
| 4 | 3 | 0 (not found) | 1 | {1: 1, 2: 2, 3: 1} |
| 5 | 1 | 1 | 2 | {1: 2, 2: 2, 3: 1} |
| 6 | 2 | 2 | 3 | {1: 2, 2: 3, 3: 1} |

**Output:** {1: 2, 2: 3, 3: 1}

---

### Time & Space Complexity

- **Time:** O(n) where n = length of input list
- **Space:** O(k) where k = number of unique elements

### Comparison

| Approach | Lines | Readability | Performance |
|----------|-------|-------------|-------------|
| if-else | 4 | More explicit | Same |
| dict.get() | 1 | More Pythonic | Same |

### Alternative: Using collections.Counter

```python
from collections import Counter

data = [1, 2, 2, 3, 1, 2]
freq = Counter(data)
print(freq)  # Counter({2: 3, 1: 2, 3: 1})
```
- Built-in Python module for counting
- Most concise, but less educational

---

## 9. Recursion Basics

**Concept:** A function that calls itself to solve smaller subproblems until it reaches a base case.

**File:** `recursionstart.py`

### What is Recursion?

Recursion breaks a problem into:
1. **Base Case** - The stopping condition (prevents infinite recursion)
2. **Recursive Case** - The function calls itself with a smaller/simpler input

---

### Example 1: Infinite Recursion (BAD)

```python
def f(n):
    if n == 0:
        return 0
    return f(n + 1)  # moves away from 0
f(5)
```

**Problem:** Starting from 5, it goes 5 -> 6 -> 7 -> ... (never reaches 0)

**Result:** Stack overflow / RecursionError

**Why it fails:**
- Base case is `n == 0`
- But `n + 1` moves AWAY from 0, not towards it

---

### Example 2: Finite Recursion (GOOD)

```python
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
countdown(5)
```

**Output:**
```
5
4
3
2
1
```

**Why it works:**
- Base case: `n == 0` (stop when we reach 0)
- Recursive case: `countdown(n - 1)` moves TOWARDS base case

#### Call Stack Visualization

```
countdown(5)  --> prints 5, calls countdown(4)
  countdown(4)  --> prints 4, calls countdown(3)
    countdown(3)  --> prints 3, calls countdown(2)
      countdown(2)  --> prints 2, calls countdown(1)
        countdown(1)  --> prints 1, calls countdown(0)
          countdown(0)  --> base case, returns
        returns
      returns
    returns
  returns
returns
```

---

### Example 3: Factorial (Classic Recursion)

**Problem:** Calculate n! = n x (n-1) x (n-2) x ... x 1

**Mathematical Definition:**
- 0! = 1 (base case)
- 1! = 1 (base case)
- n! = n x (n-1)! (recursive case)

#### Pseudocode

```
FUNCTION factorial(n):
    IF n < 0:
        ERROR "Factorial not defined for negative numbers"
    IF n == 0 OR n == 1:
        RETURN 1                   # Base case
    RETURN n * factorial(n - 1)    # Recursive case
```

#### Code Explanation

```python
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```
- **Type hints:** `n: int` input, `-> int` return type
- **Error handling:** Negative numbers raise ValueError
- **Base case:** 0! = 1! = 1
- **Recursive case:** n! = n * (n-1)!

```python
n = int(input("Enter n: "))
print("Factorial:", factorial(n))
```

#### Dry Run

**Input:** factorial(5)

| Call | n | Base Case? | Returns |
|------|---|------------|----------|
| factorial(5) | 5 | No | 5 * factorial(4) |
| factorial(4) | 4 | No | 4 * factorial(3) |
| factorial(3) | 3 | No | 3 * factorial(2) |
| factorial(2) | 2 | No | 2 * factorial(1) |
| factorial(1) | 1 | Yes | 1 |

**Unwinding the stack:**

```
factorial(1) = 1
factorial(2) = 2 * 1 = 2
factorial(3) = 3 * 2 = 6
factorial(4) = 4 * 6 = 24
factorial(5) = 5 * 24 = 120
```

**Output:** 120

#### Call Stack Diagram

```
[factorial(5)]  waiting for factorial(4)
  [factorial(4)]  waiting for factorial(3)
    [factorial(3)]  waiting for factorial(2)
      [factorial(2)]  waiting for factorial(1)
        [factorial(1)]  returns 1
      returns 2 * 1 = 2
    returns 3 * 2 = 6
  returns 4 * 6 = 24
returns 5 * 24 = 120
```

### Time & Space Complexity

| Example | Time | Space (Call Stack) |
|---------|------|--------------------|
| Countdown | O(n) | O(n) |
| Factorial | O(n) | O(n) |

**Note:** Each recursive call adds a frame to the call stack, so space is O(n).

### Key Rules for Recursion

| Rule | Description |
|------|-------------|
| 1. Base Case | Always have a stopping condition |
| 2. Progress | Each call must move towards base case |
| 3. Trust | Assume recursive call works correctly |
| 4. Stack Limit | Python default is ~1000 recursive calls |

### Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| No base case | Infinite recursion | Add stopping condition |
| Wrong direction | Never reaches base | Ensure progress towards base |
| Base case too late | Stack overflow | Check base case first |

---

## 10. Fibonacci

**Problem:** Find the nth Fibonacci number.

**Sequence:** 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

**Definition:** F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1

**File:** `fibonacci.py`

---

### Approach 1: Naive Recursion - O(2^n)

Direct implementation of the mathematical definition.

#### Pseudocode

```
FUNCTION fib(n):
    IF n < 0:
        ERROR "n must be non-negative"
    IF n == 0:
        RETURN 0
    IF n == 1:
        RETURN 1
    RETURN fib(n - 1) + fib(n - 2)
```

#### Code Explanation

```python
def fib(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
```
- **Base cases:** F(0) = 0, F(1) = 1
- **Recursive case:** F(n) = F(n-1) + F(n-2)
- Simple but very inefficient!

#### Call Tree for fib(5)

```
                    fib(5)
                   /      \
              fib(4)        fib(3)
             /     \        /     \
         fib(3)   fib(2)  fib(2)  fib(1)
         /   \     /   \   /   \
      fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
      /   \
   fib(1) fib(0)
```

**Problem:** Same values computed multiple times!
- fib(3) computed 2 times
- fib(2) computed 3 times
- fib(1) computed 5 times
- fib(0) computed 3 times

#### Time & Space Complexity (Naive)

- **Time:** O(2^n) - exponential (very slow!)
- **Space:** O(n) - call stack depth

---

### Approach 2: Memoization - O(n)

Store computed results to avoid redundant calculations.

#### Pseudocode

```
FUNCTION fib(n, memo):
    IF n < 0:
        ERROR "n must be non-negative"
    IF memo is None:
        memo = {}
    IF n IN memo:
        RETURN memo[n]             # Return cached result
    IF n == 0:
        RETURN 0
    IF n == 1:
        RETURN 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    RETURN memo[n]
```

#### Code Explanation

```python
def fib(n: int, memo=None) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")
    if memo is None:
        memo = {}
```
- Initialize memo dictionary on first call
- Using `memo=None` instead of `memo={}` avoids mutable default argument bug

```python
    if n in memo:
        return memo[n]
```
- **Key optimization:** If already computed, return cached result immediately

```python
    if n == 0:
        return 0
    if n == 1:
        return 1
```
- Base cases same as before

```python
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
```
- Compute result, store in memo, then return
- Pass memo to recursive calls so they share the cache

```python
n = int(input("Enter n: "))
print("Fibonacci:", fib(n))
```

#### Dry Run with Memoization

**Input:** fib(5)

| Call | n | memo before | Action | memo after |
|------|---|-------------|--------|------------|
| fib(5) | 5 | {} | Compute | - |
| fib(4) | 4 | {} | Compute | - |
| fib(3) | 3 | {} | Compute | - |
| fib(2) | 2 | {} | Compute | - |
| fib(1) | 1 | {} | Base case | {} |
| fib(0) | 0 | {} | Base case | {} |
| Return | 2 | - | 1+0=1 | {2: 1} |
| fib(1) | 1 | {2: 1} | Base case | {2: 1} |
| Return | 3 | - | 1+1=2 | {2: 1, 3: 2} |
| fib(2) | 2 | {2: 1, 3: 2} | **Cache hit!** | {2: 1, 3: 2} |
| Return | 4 | - | 2+1=3 | {2: 1, 3: 2, 4: 3} |
| fib(3) | 3 | {2: 1, 3: 2, 4: 3} | **Cache hit!** | - |
| Return | 5 | - | 3+2=5 | {2: 1, 3: 2, 4: 3, 5: 5} |

**Output:** 5

#### Time & Space Complexity (Memoization)

- **Time:** O(n) - each value computed only once
- **Space:** O(n) - memo dictionary + call stack

---

### Comparison

| Approach | Time | Space | fib(40) Speed |
|----------|------|-------|---------------|
| Naive | O(2^n) | O(n) | ~40 seconds |
| Memoization | O(n) | O(n) | < 1 ms |

**Why memoization is faster:**
- Naive: ~2^40 = 1 trillion operations
- Memoization: ~40 operations

### Fibonacci Reference Table

| n | F(n) |
|---|------|
| 0 | 0 |
| 1 | 1 |
| 2 | 1 |
| 3 | 2 |
| 4 | 3 |
| 5 | 5 |
| 6 | 8 |
| 7 | 13 |
| 8 | 21 |
| 9 | 34 |
| 10 | 55 |

---

## 11. Sum of Digits (Recursion)

**Problem:** Find the sum of all digits in a number using recursion.

**Example:** 1234 -> 1 + 2 + 3 + 4 = 10

**File:** `sumofdigitsrecrusion.py`

### Approach

Recursively extract the last digit and add it to the sum of remaining digits.

### Pseudocode

```
FUNCTION sum_digits(n):
    n = |n|                        # Handle negatives
    IF n == 0:
        RETURN 0                   # Base case
    RETURN (n MOD 10) + sum_digits(n DIV 10)
```

### Code Explanation

```python
def sum_digits(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)
```
- **`abs(n)`:** Handle negative numbers
- **Base case:** When n becomes 0, return 0
- **Recursive case:** Last digit + sum of remaining digits

```python
n = int(input("Enter number: "))
print("Sum of digits:", sum_digits(n))
```

### Dry Run

**Input:** sum_digits(1234)

| Call | n | n % 10 | n // 10 | Returns |
|------|---|--------|---------|----------|
| sum_digits(1234) | 1234 | 4 | 123 | 4 + sum_digits(123) |
| sum_digits(123) | 123 | 3 | 12 | 3 + sum_digits(12) |
| sum_digits(12) | 12 | 2 | 1 | 2 + sum_digits(1) |
| sum_digits(1) | 1 | 1 | 0 | 1 + sum_digits(0) |
| sum_digits(0) | 0 | - | - | 0 (base case) |

**Unwinding:**
```
sum_digits(0) = 0
sum_digits(1) = 1 + 0 = 1
sum_digits(12) = 2 + 1 = 3
sum_digits(123) = 3 + 3 = 6
sum_digits(1234) = 4 + 6 = 10
```

**Output:** 10

### Time & Space Complexity

- **Time:** O(n) where n = number of digits
- **Space:** O(n) - recursive call stack

### Iterative vs Recursive Comparison

| Approach | File | Space | Style |
|----------|------|-------|-------|
| Iterative | `sum of digits.py` | O(1) | Loop-based |
| Recursive | `sumofdigitsrecrusion.py` | O(n) | Function calls |

---

## 12. GCD - Euclidean (Recursion)

**Problem:** Find the GCD of two numbers using recursive Euclidean algorithm.

**Example:** GCD(48, 18) = 6

**File:** `gcd-euclid-recursion.py`

### Approach

Recursively apply: GCD(a, b) = GCD(b, a % b) until b becomes 0.

### Pseudocode

```
FUNCTION gcd(a, b):
    a = |a|
    b = |b|
    IF b == 0:
        RETURN a                   # Base case
    RETURN gcd(b, a MOD b)         # Recursive case
```

### Code Explanation

```python
def gcd(a: int, b: int) -> int:
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    return gcd(b, a % b)
```
- **`abs()`:** GCD is always positive
- **Base case:** When b is 0, GCD is a
- **Recursive case:** GCD(a, b) = GCD(b, a % b)

```python
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("GCD:", gcd(a, b))
```

### Dry Run

**Input:** gcd(48, 18)

| Call | a | b | a % b | Returns |
|------|---|---|-------|----------|
| gcd(48, 18) | 48 | 18 | 12 | gcd(18, 12) |
| gcd(18, 12) | 18 | 12 | 6 | gcd(12, 6) |
| gcd(12, 6) | 12 | 6 | 0 | gcd(6, 0) |
| gcd(6, 0) | 6 | 0 | - | 6 (base case) |

**Unwinding:**
```
gcd(6, 0) = 6
gcd(12, 6) = 6
gcd(18, 12) = 6
gcd(48, 18) = 6
```

**Output:** 6

### Time & Space Complexity

- **Time:** O(log(min(a, b)))
- **Space:** O(log(min(a, b))) - recursive call stack

### Iterative vs Recursive Comparison

| Approach | File | Space | Style |
|----------|------|-------|-------|
| Iterative | `gcd-hcf.py` | O(1) | While loop |
| Recursive | `gcd-euclid-recursion.py` | O(log n) | Function calls |

### Why Recursion Here?

The recursive version directly mirrors the mathematical definition:
- GCD(a, 0) = a
- GCD(a, b) = GCD(b, a mod b)

This makes it elegant and easy to understand!

---

## 13. Reverse Array (Recursion)

**Problem:** Reverse an array/list using recursion.

**Example:** [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]

**File:** `reverse array using recursion.py`

---

### Approach 1: In-Place Reversal (Two Pointers)

Swap elements from both ends, moving towards the center. Best for DSA - no extra memory!

#### Pseudocode

```
FUNCTION reverse_inplace(arr, l, r):
    IF r is None:
        r = length(arr) - 1
    
    IF l >= r:
        RETURN                     # Base case: pointers crossed
    
    SWAP arr[l] and arr[r]         # Swap outer elements
    reverse_inplace(arr, l + 1, r - 1)  # Move inward
```

#### Code Explanation

```python
def reverse_inplace(arr, l=0, r=None):
    if r is None:
        r = len(arr) - 1
```
- **Default parameters:** Start with l=0, r=last index
- `r=None` pattern avoids recalculating length on every call

```python
    if l >= r:
        return
```
- **Base case:** When pointers meet or cross, array is reversed

```python
    arr[l], arr[r] = arr[r], arr[l]
    reverse_inplace(arr, l + 1, r - 1)
```
- **Swap:** Exchange elements at left and right pointers
- **Recurse:** Move pointers inward (l+1, r-1)

```python
a = [1, 2, 3, 4, 5]
reverse_inplace(a)
print(a)  # [5, 4, 3, 2, 1]
```
- Modifies the original array (in-place)

#### Dry Run

**Input:** [1, 2, 3, 4, 5]

| Call | l | r | l >= r? | Swap | Array After |
|------|---|---|---------|------|-------------|
| 1 | 0 | 4 | No | arr[0] <-> arr[4] | [5, 2, 3, 4, 1] |
| 2 | 1 | 3 | No | arr[1] <-> arr[3] | [5, 4, 3, 2, 1] |
| 3 | 2 | 2 | Yes | - | Return (base case) |

**Output:** [5, 4, 3, 2, 1]

#### Time & Space Complexity

- **Time:** O(n) - visits each element once
- **Space:** O(n/2) = O(n) - recursive call stack

---

### Approach 2: Return New Reversed Array

Simpler logic but creates a new array (extra memory).

#### Pseudocode

```
FUNCTION reversed_copy(arr, i):
    IF i == length(arr):
        RETURN []                  # Base case: empty array
    RETURN reversed_copy(arr, i + 1) + [arr[i]]
```

#### Code Explanation

```python
def reversed_copy(arr, i=0):
    if i == len(arr):
        return []
    return reversed_copy(arr, i + 1) + [arr[i]]
```
- **Base case:** When index reaches array length, return empty list
- **Recursive case:** Reverse rest of array, then append current element
- Elements get added in reverse order during unwinding!

```python
print(reversed_copy([10, 20, 30]))  # [30, 20, 10]
```

#### Dry Run

**Input:** reversed_copy([10, 20, 30])

| Call | i | arr[i] | Returns |
|------|---|--------|----------|
| reversed_copy([...], 0) | 0 | 10 | reversed_copy(..., 1) + [10] |
| reversed_copy([...], 1) | 1 | 20 | reversed_copy(..., 2) + [20] |
| reversed_copy([...], 2) | 2 | 30 | reversed_copy(..., 3) + [30] |
| reversed_copy([...], 3) | 3 | - | [] (base case) |

**Unwinding:**
```
reversed_copy(..., 3) = []
reversed_copy(..., 2) = [] + [30] = [30]
reversed_copy(..., 1) = [30] + [20] = [30, 20]
reversed_copy(..., 0) = [30, 20] + [10] = [30, 20, 10]
```

**Output:** [30, 20, 10]

#### Time & Space Complexity

- **Time:** O(n^2) - list concatenation is O(n) each time
- **Space:** O(n) - new array + call stack

---

### Comparison

| Approach | Modifies Original | Extra Memory | Time | Best For |
|----------|-------------------|--------------|------|----------|
| In-Place | Yes | O(1)* | O(n) | DSA interviews |
| New Copy | No | O(n) | O(n^2) | When original needed |

*O(1) extra memory (excluding call stack)

### Which to Use?

- **In-place:** When you don't need the original array (most DSA problems)
- **New copy:** When you need to keep the original array intact

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
7. [x] Find factors of a number
8. [x] Store frequency in dictionary
9. [x] Recursion basics (factorial, countdown)
10. [x] Fibonacci (naive + memoization)
11. [x] Sum of digits (recursion)
12. [x] GCD - Euclidean (recursion)
13. [x] Reverse array (recursion)

---

*Last Updated: January 8, 2026*
