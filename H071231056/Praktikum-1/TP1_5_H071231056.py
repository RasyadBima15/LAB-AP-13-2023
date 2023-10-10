# Membuat program yang mengubah detik kedalam format jam:menit:detik

print("\nKonversi detik ke jam\n")

jumlah_detik = int(input("masukan jumlah detik : "))
"""jadi pertama tama detiknya kita bagi(//) 3600 dalam bil.bulat untuk cari jamnya,
lalu sissa detiknya untuk mencari menit dan detiknya"""
jam = jumlah_detik //3600
# print(jam)
# disitu kan pasti ada sisa detiknya, maka kita pake sisa detiknya untuk mencari menit dan detik
sisa_detik = jumlah_detik % 3600
# print(sisa_detik)
menit = sisa_detik // 60
# cari menit
# print(menit)
detik = sisa_detik % 60
"""bukannya sisa detiknya dipake dimenit? iya dipake, namun di detiknya kita cari
sisa detiknya lagi setelah dipake dimenit"""
# cari si detiknya
# print(detik)

hasil = f"{jam:02d}:{menit:02d}:{detik:02d}"
print(hasil)




