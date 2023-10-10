while True:
    try:
        M = float(input())
        if 0 <= M < 360:
            detik = M * 240 
            jam = ((detik // 3600) + 6) % 24
            sisa_detik = detik % 3600
            menit = sisa_detik // 60
            detik = sisa_detik % 60

            if jam >= 0 and jam < 6:
                waktu = "Selamat Malam"
            elif jam >= 6 and jam < 12:
                waktu = "Selamat Pagi"
            elif jam >= 12 and jam < 18:
                waktu = "Selamat Siang"
            else:
                waktu = "Selamat Sore"

            print(waktu)
            print(f'{int(jam):02}:{int(menit):02}:{int(detik):02}')
        else:
            print('Invalid input')
    except EOFError:
        print('Data error')
        break

