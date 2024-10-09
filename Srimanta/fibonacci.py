def fibonacci(n):
    """
    Generate the Fibonacci series up to the nth number.
    
    Args:
        n (int): The number of Fibonacci numbers to generate.
    
    Returns:
        list: A list of Fibonacci numbers.
    """
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series


# Example usage:
n = 10
print(fibonacci(n))