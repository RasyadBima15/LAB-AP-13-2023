print('Menghitung luas permukaan dan keliling segitiga')

x=float(input('Panjang sisi X : '))
y=float(input('Panjang sisi Y : '))

z = (x ** 2 + y ** 2) ** 0.5

luas = 1/2 * x * y
keliling = x + y + z

luasFixed=format(luas, ".2f")
kelilingFixed=format(keliling, ".2f")

print('Luas Permukaan :', luasFixed)
print('Keliling :', kelilingFixed)