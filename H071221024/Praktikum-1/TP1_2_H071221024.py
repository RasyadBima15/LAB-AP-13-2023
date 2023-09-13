print("Konversi Suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit")

celcius = float(input("Masukkan Suhu dalam Celcius : "))
celciusFixed = int(celcius)

kelvin = celciusFixed + 273
reamur = 4/5 * celciusFixed
fahrenheit = 9/5 * celciusFixed + 32

print(f"Hasil konversi dari suhu {celciusFixed} derajat Celcius ke Kelvin adalah : {int(kelvin)}K")
print(f"Hasil konversi dari suhu {celciusFixed} derajat Celcius ke Reamur adalah : {int(reamur)}R")
print(f"Hasil konversi dari suhu {celciusFixed} derajat Celcius ke Fahrenheit adalah : {int(fahrenheit)}F")