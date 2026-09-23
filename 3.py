n = int(input("Masukan berapa banyak nilai fibonacci: "))

a, b = 0, 1
count = 0

print("Seri Fibonacci:")
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
