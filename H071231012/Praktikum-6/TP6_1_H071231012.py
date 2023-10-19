print ("Selamat datang silahkan input data anda")
nama = input("Masukkan nama anda : ")
umur = int(input("Masukkan umur anda : "))
alamat = input("Masukkan alamat anda : ")
print()
print("="*50)

while True :
    data = {
                1 : f"Nama : {nama}",
                2 : f"Umur : {umur}",
                3 : f"Alamat : {alamat}"
        }
    print(f"Selamat datang {nama} silakan pilih opsi")
    print("="*50)
    print("1. Detail anda.\n2. Ubah nama.\n3. Ubah umur.\n4. Ubah alamat\n5. Keluar")
    print("="*50)
    pilihan = input("Masukkan pilihan : ")
    match pilihan :
        case "1" :
            print("="*50)
            print("Detail anda adalah")
            print(data[1])
            print(data[2])
            print(data[3])
            print()
            print("="*50)
        case "2" :
            nama = input("silahkan input nama baru : ")
            Nama = nama
            print("Data anda sukses diperbarui\n")
            print("="*50)
        case "3" :
            umur = input("silahkan input umur baru : ")
            Umur = umur
            print("Data anda sukses diperbarui\n")
            print("="*50)
        case "4" :
            alamat = input("silahkan input alamat baru : ")
            Alamat = alamat
            print("Data anda sukses diperbarui\n")
            print("="*50)
        case "5" :
            print(f"Selamat tinggal {nama}")
            break
        case _:
            print("inputan tidak valid mohon mencoba kembali!")