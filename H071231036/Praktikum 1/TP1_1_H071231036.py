x = float(input("Masukkan panjang sisi X: "))
y = float(input("Masukkan panjang sisi Y: "))

z = (x**2 + y**2)**0.5

s = (x + y + z) // 2
luas = (s * (s - x) * (s - y) * (s - z))**0.5

keliling = x + y + z

print(f"Luas segitiga XYZ: {luas:.2f}")
print(f"Keliling segitiga XYZ: {keliling:.2f}")