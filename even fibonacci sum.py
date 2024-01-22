def evenfib(n):
    fib1, fib2 = 0, 1
    even_sum = 0

    while fib2 <= n:
        if fib2 % 2 == 0:
            even_sum += fib2

        fib1, fib2 = fib2, fib1 + fib2

    print(even_sum)

# Take input from the user
n = int(input())
evenfib(n)
