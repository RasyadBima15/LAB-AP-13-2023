print("Konversi detik ke jam")

detik_awal = int(input("Masukkan jumlah detik: "))
jam = int(detik_awal // 3600)
menit = int(detik_awal - (jam*3600)) // 60
detik = int(detik_awal - (jam*3600) - (menit*60))

print("%02d:%02d:%02d" % (jam, menit, detik))

#Other Way
# print("Konversi detik ke jam")

# detik_awal = int(input("Masukkan jumlah detik: "))

# jam = detik_awal // 3600
# sisa_detik_setelah_jam = detik_awal % 3600

# menit = sisa_detik_setelah_jam // 60
# detik = sisa_detik_setelah_jam % 60

# print("%02d:%02d:%02d" % (jam, menit, detik))