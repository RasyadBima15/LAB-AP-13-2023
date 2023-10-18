print("selamat datang untuk memulai silahkan input data anda")
nama1 = input("input nama : ")
umur = input("input umur : ")
alamat1 = input("input alamat : ")
print()
print("=" *50)

while True :
    data = {
                1 : f"Nama : {nama1}",
                2 : f"Umur : {umur}" ,
                3 : f"Alamat : {alamat1}"
        }
    print(f"Selamat datang {nama1} silahkan pilih opsi")
    print("=" *50)
    print("1. Detail Anda.\n2. Ubah Nama.\n3. Ubah Umur.\n4. Ubah Alamat\n5. Keluar")
    print("=" *50)
    pilihan = input("masukkan pilihan : ")
    match pilihan :
        case "1" :
            print("=" *50)
            print("Detail Anda Adalah")
            print(data[1])
            print(data[2])
            print(data[3])
            print()
            print("=" *50)
        case "2" :
            nama = input("silahkan imput nama baru : ")
            nama1 = nama
            print("Data anda sukses di perbarui!!\n")
            print('=' *50)
        case "3" :
            umur1 = input("silahkan imput umur baru : ")
            umur = umur1
            print("Data anda sukses di perbarui!!\n")
            print("=" *50)
        case "4" :
            alamat = input ("silahkan imput alamat baru : ")
            alamat1 = alamat
            print("Data anda sukses di perbarui!!\n")
            print("=" *50)
        case "5" :
            print(f"selamat tinggal {nama1}")
            break
        case _:
            print("inputan tidak valid !!")
            print("=" *50)