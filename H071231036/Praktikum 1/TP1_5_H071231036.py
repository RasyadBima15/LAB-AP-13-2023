detik = int(input("Masukkan jumlah detik: "))

jam = detik // 3600
detik_sisa = detik % 3600
menit = detik_sisa // 60
detik_sisa = detik_sisa % 60

jam_str = str(jam).zfill(2)
menit_str = str(menit).zfill(2)
detik_str = str(detik_sisa).zfill(2)

print(f"Hasil konversi: {jam_str}:{menit_str}:{detik_str}")
