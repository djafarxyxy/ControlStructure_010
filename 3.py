n = int(input("Masukan berapa banyak nilai fibonacci: "))

a, b = 0, 1


print("Seri Fibonacci:")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
  
