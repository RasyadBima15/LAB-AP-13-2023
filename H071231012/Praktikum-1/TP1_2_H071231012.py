print('masukkan suhu dalam celcius ke kelvin, reamur, dan fahrenheit')
celcius = int(input("masukkan suhu dalam celcius : "))
kelvin = celcius + 273
reamur = 4/5 * celcius
fahrenheit = 9/5 * celcius + 32

print(f"hasil konversi dari suhu celcius ke kelvin adalah : {kelvin}k")
print(f"hasil konversi dari suhu celcius ke reamur adalah : {int(reamur)}r")
print(f"hasil konversi dari suhu celcius ke fahrenheit adalah : {fahrenheit}f")