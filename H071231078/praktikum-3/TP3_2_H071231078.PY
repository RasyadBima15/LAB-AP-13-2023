harga_barang = int(input())
jumlah_uang = int(input())
n = jumlah_uang-harga_barang
x = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
y = [0, 0, 0, 0, 0, 0, 0]

for i in range(len(x)):
    while n >= x[i]:
        n -= x[i]
        y[i] += 1
    
for i in range(len(x)):
    print(y[i],"uang sejumlah", x[i])