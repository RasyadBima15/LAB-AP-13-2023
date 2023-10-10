# program mengubah besaran suhu celcius ke beberapa skala lain seperti Kelvin, Reamur, dan Fahrenheit.
print("konversi suhu dari celcius ke Kelvin, Reamur dan Fahrenheit")
c = int(input("masukkan suhu dalam celcius : "))

k = c + 273.15
r =  (c * 4) / 5
f = (c * 9/5) + 32

print(f"Hasil konversi dari suhu {c} derajat Celcius ke Kelvin adalah: {int(k)}K")
print(f"Hasil konversi dari suhu {c} derajat Celcius ke Reamur adalah: {int(r)}R")
print(f"Hasil konversi dari suhu {c} derajat Celcius ke Fahrenheit adalah: {int(f)}F")