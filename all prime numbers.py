def primenumbers(n):
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):  # Check up to square root of i
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i)

n = int(input())
primenumbers(n)
