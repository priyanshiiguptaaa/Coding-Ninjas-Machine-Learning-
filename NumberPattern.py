n = int(input())

for x in range(1, n + 1):
    # Print 1 to x
    for i in range(1, x + 1):
        print(i, end="")
    
    # Print (n-x) spaces
    for i in range(n - x):
        print(" ", end="")
    
    # Print (n-x) spaces followed by x..1
    for i in range(x, 0, -1):
        print(i, end="")
    
    print()  # Move to the next line for the next row
