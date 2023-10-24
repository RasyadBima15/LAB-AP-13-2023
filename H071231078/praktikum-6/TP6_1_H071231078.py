print("Selamat datang untuk memulai, silahkan input data anda")
a = input("Input nama   : ")
b = input("Input umur   : ")
c = input("Input alamat : ")

dict1 = {"nama": a, "umur": b, "alamat": c}

while True:
    print(" ")
    print("==================================================")
    print(f"Selamat datang {dict1['nama']} silahkan pilih opsi")
    print("==================================================")

    print("1. Detail anda\n2. Ubah Nama\n3. Ubah Umur\n4. Ubah Alamat\n5. Keluar")
    print("==================================================")

    d = int(input("Input opsi: "))

    if d == 1:
        print("==================================================")
        print("Data anda adalah")
        print(f"Nama   : {dict1.get('nama')} ")
        print(f"Umur   : {dict1.get('umur')} ")
        print(f"Alamat : {dict1.get('alamat')} ")
    elif d == 2: 
        dict1["nama"] = input("input nama baru : ")
        print("Data anda sukses di diperbarui")
    elif d == 3: 
        dict1["umur"] = input("input umur baru : ")
        print("Data anda sukses di diperbarui")
    elif d == 4: 
        dict1["alamat"] = input("input alamat baru : ")
        print("Data anda sukses di diperbarui")
    elif d == 5: 
        print(f"Selamat Tinggal {dict1.get('nama')}")
        break
    
    

