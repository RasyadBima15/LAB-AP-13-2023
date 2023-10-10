# Program mengkonversi suhu dari skala Celcius ke skala suhu lainnya(Fahrenheit, Reamor, dan Kelvin)

print("\nprogram mengkonversi suhu celcius ke suhu kelvin, reamor dan fahrenheit\n".upper())

celcius = int(input('masukan suhu dalam celcius :'))

# kelvin
kelvin = celcius + 273.15
print(f"Hasil konversi dari {celcius} derajat Celcius ke Kelvin adalah",int(kelvin),"K")

# reamur
reamur = (4 / 5) * celcius
print(f"Hasil konversi dari {celcius} derajat Celcius ke Reamur adalah",int(reamur),"R")

# fahrenheit
fahrenheit = ((9 / 5) * celcius) + 32
print(f"Hasil konversi dari {celcius} derajat Celcius ke Fahrenheit adalah",int(fahrenheit),"F")