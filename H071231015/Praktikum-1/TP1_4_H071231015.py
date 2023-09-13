print(f'Pengujian jenis karakter')
print(f'------------------------')
x = input(f'Karakter = ')

kapital = x >= "A" and x <= "Z"
kecil = x >= "a" and x <= "z"
angka = x >= "0" and x <= "9"

print(f'Huruf kapital? {kapital}')
print(f'Huruf kecil? {kecil}')
print(f'Angka? {angka}')

 