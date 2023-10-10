harga_barang = int(input())
uang_dibayarkan = int(input())

if harga_barang > uang_dibayarkan:
    print('Uang tidak cukup')
    exit()
else:
    kembalian = uang_dibayarkan - harga_barang

uang_pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500]

for pecahan in uang_pecahan:
    jumlah = kembalian // pecahan
    print(f"{jumlah} uang sejumlah Rp.{pecahan}")
    kembalian = kembalian % pecahan