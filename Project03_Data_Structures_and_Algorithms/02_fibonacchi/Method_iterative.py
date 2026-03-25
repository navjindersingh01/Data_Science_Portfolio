# Fibonacci Series

def fibonacci_iterative(n:int) -> list[int]:
    if (n == 0):
        return []
    
    if (n == 1):
        return [0]
    
    fib = [0,1]

    
    for i in range(2,n):
        fib.append(fib[-1] + fib[-2])

    return fib

def fibonacci_optimized(n):
    a, b = 0,1
    fib = []
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    
    return fib

def fibonacci_recursive(n):
    if (n <= 1):
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_sum(fibonacci_list:list[int]) -> int:
    return sum(fibonacci_list)

def fibonacci_size(n:int) -> list[int]:
    """
        This function return the number of letter it has.
    """
    size_list = []
    series = fibonacci_optimized(n)

    for i in series:
        size_list.append(len(str(i)))

    return size_list
    