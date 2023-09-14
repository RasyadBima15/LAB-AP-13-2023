# Menghitung luas permukaan segitiga dan keliling segitiga XYZ
"""dimana X sebagai tinggi, y sebagai alas dan Z sebagai sisi miring"""

print("\nMenghitung luas permukaan dan keliling segitiga\n")
# diketahui
X = float(input("masukan sisi X = "))
Y = float(input("masukan sisi Y = "))
Z = ((X ** 2) + (Y ** 2)) ** 0.5
# print(Z)
Luas_permukaan  = 1/2 * X * Y
Keliling        =  X + Y + Z
print(f"\nJika nilai Sisi X, Y, dan Z adalah {X}, {Y}, dan {Z}, maka:\n")     
print(f"Luas permukaan segitiga XYZ adalah {Luas_permukaan:.2f}")
print(f"Keliling segitiga XYZ adalah {Keliling:.2f}\n")

