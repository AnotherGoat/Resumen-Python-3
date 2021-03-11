def factorial(n):
    if n < 0:
        raise ValueError
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # 5 * 4 * 3 * 2 * 1
print(factorial(0))  # 1
print(factorial(-10))