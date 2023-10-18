bilangan =map(int, input("Masukkan beberapa angka : ").split())
genap = []
ganjil = []
modulo5 = []
for i in bilangan :
    if i % 2 == 0:
        genap.append(i)
    if i % 2 != 0:
        ganjil.append(i)
    if i % 5 == 0:
        modulo5.append(i)

print(f"Angka Genap : {genap}")
print(f"Angka Ganjil : {ganjil}")
print(f"Angka Yang Habis Dibagi 5 : {modulo5}")
