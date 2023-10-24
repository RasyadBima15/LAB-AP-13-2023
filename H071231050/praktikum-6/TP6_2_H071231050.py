kata1 = map(int, input("Input array ke-1 : ").split())
kata2 = map(int, input("Input array ke-2 : ").split())
hasil1 = []
for i in kata1 :
    hasil1.append(i)
hasil2 = []
for i in kata2 :
    hasil2.append(i)

a,b = set(hasil1),set(hasil2)
jumlah_samaan = len(a & b)
char_samaan = list(a & b)
x = ''
for i in range(jumlah_samaan) :
    x += str(char_samaan[i]) + ","

hasil = x[:-1]

if jumlah_samaan != 0 :
    print (f'Terdapat {jumlah_samaan} buah duplikat yaitu ({hasil}) ')
else :
    print ("Tidak ada duplikat ditemukan.")
