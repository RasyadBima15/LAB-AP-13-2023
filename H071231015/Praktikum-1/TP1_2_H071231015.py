print(f'Konversi Suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit')
c = int(input(f'Masukkan suhu dalam Celcius : '))
k = c + 273
r = 4/5 * c
f = 32 + c * 9/5
print(f'\nHasil konversi dari suhu {c} derajat Celcius ke Kelvin adalah : {int(k)}K')
print(f'\nHasil konversi dari suhu {c} derajat Celcius ke Reamur adalah : {int(r)}R')
print(f'\nHasil konversi dari suhu {c} derajat Celcius ke Fahrenheit adalah : {int(f)}F')