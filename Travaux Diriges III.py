#Q1. a. Sequential (Iterative) Fibonacci Algorithm
def fibonacci(n):
    """
    Calculates the nth Fibonacci number using a sequential algorithm.

    Args:
    n (int): The position of the Fibonacci number to calculate.

    Returns:
    int: The nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_prev = 0
        fib_curr = 1
        for i in range(2, n + 1):
            fib_next = fib_prev + fib_curr
            fib_prev = fib_curr
            fib_curr = fib_next
        return fib_curr

# Example usage:
n = 30
result = fibonacci(n)
print(f"Fibonacci({n}) = {result}")

#Q1. a. Recursive Fibonacci Algorithm
def fibonacci_recursive(n):
    """
    Calculates the nth Fibonacci number using a recursive algorithm.

    Args:
    n (int): The position of the Fibonacci number to calculate.

    Returns:
    int: The nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Example usage:
n = 10
result = fibonacci_recursive(n)
print(f"Fibonacci({n}) = {result}")





#Q2. b. Test Fibonacci Edge Cases
def test_fibonacci_edge_cases(fibonacci):
    """
    Verifies Fibonacci edge cases.

    Args:
    fibonacci (function): The Fibonacci function to test.

    Raises:
    AssertionError: If edge cases fail.
    """
    assert fibonacci(0) == 0, "Fibonacci(0) failed"
    assert fibonacci(1) == 1, "Fibonacci(1) failed"

# Example usage:
def fibonacci(n):
    if n <= 1:
        return n
    else:
        fib_prev = 0
        fib_curr = 1
        for i in range(2, n + 1):
            fib_next = fib_prev + fib_curr
            fib_prev = fib_curr
            fib_curr = fib_next
        return fib_curr

test_fibonacci_edge_cases(fibonacci)
print("Edge cases passed")

#Q2. b. Test Fibonacci Small Values
def test_fibonacci_small_values(fibonacci):
    """
    Verifies Fibonacci small values.

    Args:
    fibonacci (function): The Fibonacci function to test.

    Raises:
    AssertionError: If small values fail.
    """
    assert fibonacci(5) == 5, "Fibonacci(5) failed"
    assert fibonacci(10) == 55, "Fibonacci(10) failed"

# Example usage:
def fibonacci(n):
    if n <= 1:
        return n
    else:
        fib_prev = 0
        fib_curr = 1
        for i in range(2, n + 1):
            fib_next = fib_prev + fib_curr
            fib_prev = fib_curr
            fib_curr = fib_next
        return fib_curr

test_fibonacci_small_values(fibonacci)
print("Small values passed")

#Q2. b. Test Fibonacci Larger Values
def test_fibonacci_larger_values(fibonacci):
    """
    Verifies Fibonacci larger values.

    Args:
    fibonacci (function): The Fibonacci function to test.

    Raises:
    AssertionError: If larger values fail.
    """
    assert fibonacci(30) == 832040, "Fibonacci(30) failed"
    assert fibonacci(40) == 102334155, "Fibonacci(40) failed"

# Example usage:
def fibonacci(n):
    if n <= 1:
        return n
    else:
        fib_prev = 0
        fib_curr = 1
        for i in range(2, n + 1):
            fib_next = fib_prev + fib_curr
            fib_prev = fib_curr
            fib_curr = fib_next
        return fib_curr

