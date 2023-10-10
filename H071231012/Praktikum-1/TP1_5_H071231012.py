print("konversi detik ke jam")
detik = int(input("masukkan jumlah detik : "))

jam = int(detik // 3600) 
sisa_detik = int(detik % 3600 ) 
menit = int(sisa_detik // 60) 
detik = int(sisa_detik % 60)


print("%02d:%02d:%02d" % (jam, menit, detik))