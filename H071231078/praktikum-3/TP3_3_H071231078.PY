while True:
    x = input()
    if x == "end of file":
        break
    
    x = float(x)
    totalDetik = int(x*240)
    jam = totalDetik // 3600
    sisaDetik = totalDetik % 3600
    menit = sisaDetik // 60
    detik = sisaDetik % 60

    if 270 < x <= 285:
        print("selamat pagi")
        print(f"{0:02d}:{menit:02d}:{detik:02d}")
    elif 285 < x <= 300:
        print("selamat pagi")
        print(f"{1:02d}:{menit:02d}:{detik:02d}")
    elif 300 < x <= 315:
        print("selamat pagi")
        print(f"{4:02d}:{menit:02d}:{detik:02d}")
    elif 315 < x <= 330:
        print("selamat pagi")
        print(f"{5:02d}:{menit:02d}:{detik:02d}")
    elif 330 < x <= 345:
        print("selamat pagi")
        print(f"{5:02d}:{menit:02d}:{detik:02d}")
    elif 345 < x < 360:
        print("selamat pagi")
        print(f"{5:02d}:{menit:02d}:{detik:02d}")
    elif x == 360:
        print("selamat pagi")
        print(f"{6:02d}:{0:02d}:{0:02d}")
    else:
        n = jam + 6
        if 6 <= n <= 9:
            print("selamat pagi")
        elif 10 <= n <= 15:
            print("selamat siang")
        elif 16 <= n <= 18:
            print("selamat sore")
        elif 19 <= n <= 24:
            print("selamat malam")
        print(f"{n:02d}:{menit:02d}:{detik:02d}")