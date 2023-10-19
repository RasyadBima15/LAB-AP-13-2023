bilangan = input("Masukkan beberapa angka : ").split()#untuk memisahkan data
genap = []
ganjil = []
modulo5 = []
for i in bilangan :
    x = int(i)
    if x % 2 == 0:
        genap.append(x)
        if x % 5 == 0:
            modulo5.append(x)#untuk menambah nilai baru
    elif x % 2 != 0: 
        ganjil.append(x)
        if x % 5 == 0:
            modulo5.append(x)

print(f'Angka genap : {genap}')
print(f'Angka ganjil : {ganjil}')
print(f'Angka yang habis dibagi 5 : {modulo5}')