n = int(input("Enter rows: "))

# upper part
for i in range(n):
    for j in range(n - i):
        print("*", end="")
    for j in range(2 * i):
        print(" ", end="")
    for j in range(n - i):
        print("*", end="")
    print()

# lower part
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    for j in range(2*(n-i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()