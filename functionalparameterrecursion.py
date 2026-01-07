#Function parameters (basic)

def add(a, b):   # a and b are parameters
    return a + b

add(3, 5)        # 3 and 5 are arguments


#Functional parameters (higher-order functions)

def apply_twice(f, x):
    return f(f(x))

def inc(n):
    return n + 1

print(apply_twice(inc, 10))  # 12

