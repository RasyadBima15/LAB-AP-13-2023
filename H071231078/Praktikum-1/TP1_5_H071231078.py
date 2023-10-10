print("konversi detik ke jam")

x = int(input("Masukkan jumlah detik: "))

a = x // 3600
x %= 3600

b = x // 60
c = x % 60

print(f"{a:02}:{b:02}:{c:02}")

