kata1 = input("input array ke-1 : ").split()#untuk memisahkan data
kata2 = input("input array ke-2 : ").split()
hasil1 = []
for i in kata1 :
    x = int(i)
    hasil1.append(x)
hasil2 = []
for i in kata2 :
    x = int(i)
    hasil2.append(x)#untuk menambah nilai baru kedalam list

a,b = set(hasil1),set(hasil2) 
jumlahsamaan = len(a & b)
charsamaan = tuple(a & b)
hasil = ""
for i in charsamaan: 
    hasil += str(i)
if jumlahsamaan == 1 :
    print(f'terdapat {jumlahsamaan} buah duplikat yaitu ({hasil})')
elif jumlahsamaan > 1 :
    print(f'terdapat {jumlahsamaan} buah duplikat yaitu {charsamaan}')
else : 
    print('tidak ada duplikat ditemukan')