# Input n value
n = int(input("Enter a value for n: "))

for i in range(1, n+1):
    for j in range(i):
        print(i, end=" ")
    print()
