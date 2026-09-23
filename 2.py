a = int(input("angka pertama: "))
b = int(input("angka kedua: "))
c = int(input("angka ketiga: "))

if a > b and a > c:
    print("angka terbesar:", a)
elif b > a and b > c:
    print("angka terbesar:", b)
elif c > a and c > b:
    print("angka terbesar:", c)
else:
    print("tidak ada angka terbesar")
