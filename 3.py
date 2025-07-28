# Input the number of terms
n = int(input("Enter how many Fibonacci numbers you want: "))

a, b = 0, 1
count = 0

print("Fibonacci series:")
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
