def fibonacci(n):
    """Calculate Fibonacci numbers"""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(3))
