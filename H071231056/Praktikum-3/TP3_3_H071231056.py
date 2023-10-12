print("\nMengubah sudut(dalam derajat) ke jam, menit, dan detik")
while True:

    try:
        M = float(input("\nM : "))
        
        if M < 0 or M > 360:
            print("Nilai derajat harus diantara 0 dan 360")
            continue
    
    # Hitung jam, menit, dan detik
        # dengan asumsi 1 derajat = 240 detik,
        jumlah_detik = int(M*240) # dikali untu mendapatan jumlah detik
        # pake rumus pratikum 1 no 5
        jam = 6 + (jumlah_detik // 3600)   
        if jam > 24:
             jam %= 24

        sisa_detik = jumlah_detik % 3600

        menit = sisa_detik // 60 

        detik = sisa_detik % 60 
        
    # Konversi waktu menjadi format HH:MM:SS
        waktu = f"{int(jam):02d}:{int(menit):02d}:{int(detik):02d}"
    
    # Menentukan waktu hari
        if jam < 12 :
             waktu_hari = "Selamat Pagi"
            
        elif jam < 15:
             waktu_hari = "Selamat Siang"
            
        elif jam < 18: 
             waktu_hari = "Selamat Sore"

        else:
             waktu_hari = "Selamat Malam"
            
        print(waktu_hari,"\n",waktu)

    except EOFError:# dengan Ctrl + Z
            print("EOFError terdeteksi. Program berakhir.")
            break
    except ValueError :
         print("Input harus angka(nilai) derajat harus antara 0 dan 360")

    
    