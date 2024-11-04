def fibonacci(n):
    if n == 0 or n == 1:
        return True
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
    return b == n


x = int(input("Enter a number: "))

fib = fibonacci(x)

if fib:
    print("O número é um número de Fibonacci")
else:
    print("O número não é um número de Fibonacci")
