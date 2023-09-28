while True:
    try: #kode yg menghasilkan pengecualian
        posisi_input = input()
        if posisi_input.lower() == 'end of file': #
            break

        posisi = float(posisi_input)  

        if 0 <= posisi < 360:
            detik = int(posisi / 360 * 24 * 3600)
            jam = (detik // 3600 + 6) % 24
            detik %= 3600
            menit = detik // 60
            detik %= 60

            if 6 <= jam < 10:
                waktu_selamat = 'Selamat Pagi'
            elif 10 <= jam < 15:
                waktu_selamat = 'Selamat Siang'
            elif 15 <= jam < 18:
                waktu_selamat = 'Selamat Sore'
            else:
                waktu_selamat = 'Selamat Malam'

            print(waktu_selamat)
            print(f"{jam:02}:{menit:02}:{detik:02}")
        else:
            print("Posisi diluar batas (0 - 360).")

    except ValueError: #menangani pengecualian
        print("Input tidak valid.")