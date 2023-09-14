panjang_sisi_X = float(input("panjang sisi X: "))
panjang_sisi_Y = float(input("panjang sisi Y: "))

luas_segitiga = 0.5 * panjang_sisi_X * panjang_sisi_Y

panjang_sisi_Z = (panjang_sisi_X**2 + panjang_sisi_Y**2) ** 0.5

keliling = (panjang_sisi_X + panjang_sisi_Y + panjang_sisi_Z)

print (f"luas_permukaan : {luas_segitiga:.2f}")
print (f"keliling: {keliling:.2f}")
