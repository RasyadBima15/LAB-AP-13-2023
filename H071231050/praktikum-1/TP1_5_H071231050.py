# nomor 5
print("konversi detik menjadi jam")
angka = int (input("masukkan jumlah detik = "))

jam = angka // 3600
if jam == 0 :
    menit = angka // 60
    detik = angka % 60

else :
    sisa_detik = angka % (jam * 3600)
    menit = sisa_detik // 60
    detik = sisa_detik % 60

print('{:02d}:{:02d}:{:02d}'.format(jam, menit, detik))