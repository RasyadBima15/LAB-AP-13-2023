import math

# program menghitung luas dan keliling segitiga
print("menghitung luas dan keliling segitiga")
x = float(input("panjang sisi x : "))
y = float(input("panjang sisi y : "))

# memasukkan rumus pythagoras untuk mencari sisi z pada variable z
z = math.sqrt((x**2 + y**2))

luas = 0.5 * x * y
keliling = x + y + z

print(f"luas permukaan : {luas:.2f}")
print(f"keliling : {keliling:.2f}")



