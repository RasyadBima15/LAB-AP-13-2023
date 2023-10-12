harga_barang = int(input("harga barang = "))
uang_anda = int(input("uang_anda = "))
kembalian = uang_anda - harga_barang 
total = 0 
print("\nKembalian anda adalahhhh")

pecahan_uang = [100000,50000,20000,10000,5000,2000,1000]# ini yang tersedia
for i in pecahan_uang:
    sisa = kembalian // i # hitung sisi pecahannya
    total += (sisa * i)
    # print(sisa)
    if sisa >= 0:
        print(f"{sisa} sejumlah Rp. {i}")
        kembalian -= (sisa * i) #mengurangi kembalian dengan pecahan sisa
   

if kembalian < 1000:
    print(f"\nKembalian Rp. {kembalian}  anda disaluarkan sebagai sedekah ")
    
print(f"\ntotal kembalian anda sebesar Rp. {total}\n")

