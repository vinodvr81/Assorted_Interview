from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Outputs: 55
@lru_cache(maxsize=128)
def n_fibonacci(n):
    num1 = 0
    num2 = 1
    next_number = num2
    count = 1

    while count <= n:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
    return next_number

print(n_fibonacci(10))  # Outputs: 55