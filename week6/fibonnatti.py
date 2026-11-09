def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fibonacci_recursion(n):
    if n <= 1:
        return n
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


if __name__ == "__main__":
    print(fibonacci_recursion(10))
