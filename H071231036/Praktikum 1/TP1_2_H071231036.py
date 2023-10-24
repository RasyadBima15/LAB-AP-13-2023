print('Konservasi Suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit')
celcius = float(input('Masukkan Suhu dalam Celcius : '))

kelvin = celcius+273
reamur = int(4/5*celcius)
fahrenheit = int((9/5*celcius)+32)

print(f"Hasil konversi dari suhu {celcius} derajat Celcius ke Kelvin adalah : {kelvin}K ")
print(f"Hasil konversi dari suhu {celcius} derajat Celcius ke Kelvin adalah : {reamur}R ")
print(f"Hasil konversi dari suhu {celcius} derajat Celcius ke Kelvin adalah : {fahrenheit}F ")
