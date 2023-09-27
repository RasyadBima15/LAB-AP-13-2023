while True :
    posisi = input("masukkan posisi matahari : ")

    if posisi == "end of file" :

        break

    posisi = float(posisi)
    detik = int(posisi * 240)
    jam = (detik // 3600 + 6) % 24
    n = detik % 3600
    menit, detik = n // 60 , n % 60

    if 6 <= jam < 10 :
        print ("selamat pagi")
    elif 10 <= jam < 15 :
        print ("selamat siang") 
    elif 15 <= jam < 18 :
        print ("selamat sore")
    elif 18 <= jam < 24 or 0 <= jam < 6 :
        print ("selamat malam")

    print (f'{jam:02}:{menit:02}:{detik:02}')
    



    # if jam >= 24 :
    #     jam = jam  % 24