x = float(input(f'Masukkan panjang sisi X segitiga: '))
y = float(input(f'Masukkan panjang sisi Y segitiga: '))
z = (x ** 2 + y ** 2) ** (1/2)
luas_permukaan = x * y * (1/2)
keliling = x + y + z
print('\nLuas Permukaan = ' + format(luas_permukaan,'.2f'))
print('\nKeliling = ' + format(keliling,'.2f'))