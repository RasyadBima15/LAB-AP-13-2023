harga_barang = int(input("Masukkan harga barang: "))
uang_dibayarkan = int(input("Masukkan nilai uang yang dibayarkan: "))

kembalian = uang_dibayarkan - harga_barang

pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

for pecahan in pecahan_uang:
    jumlah = kembalian // pecahan  
    kembalian %= pecahan  
    
    print(f"{jumlah} uang sejumlah Rp.{pecahan}")   
    
  
