harga_barang = int(input('Masukkan harga barang : '))
jumlah_uang = int(input('Masukkan jumlah uang : '))

kembalian = jumlah_uang - harga_barang

pecahan_uang = [100000,50000,20000,10000,5000,2000,1000]

for pecahan in pecahan_uang:
    jumlah_pecahan = kembalian // pecahan #bilangan bulat
    kembalian %= pecahan
    print(f'{jumlah_pecahan} uang sejumlah Rp. {pecahan}')