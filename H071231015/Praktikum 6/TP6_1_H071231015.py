data_detail = {
    "Nama": "",
    "Umur": "",
    "Alamat": ""
}

def ubah(data, kunci, baru):
    data[kunci] = baru
    print("Data anda sukses di perbarui")

def tampilkan(data):
    print("\nData anda adalah")
    print("Nama:", data["Nama"])
    print("Umur:", data["Umur"])
    print("Alamat:", data["Alamat"])

print("Selamat datang! Untuk memulai, silahkan input data anda.")
data_detail["Nama"] = input("Input nama: ")
data_detail["Umur"] = input("Input umur: ")
data_detail["Alamat"] = input("Input alamat: ")

while True:
    print("=" * 50)
    print(f"Selamat datang {data_detail['Nama']}. Silahkan pilih opsi")
    print("=" * 50)
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("=" * 50)
    opsi = input("Input opsi: ")
    print("=" * 50)

    if opsi == "1":
        tampilkan(data_detail)
    elif opsi == "2":
        nama_baru = input("Silahkan input nama baru: ")
        ubah(data_detail, "Nama", nama_baru)
    elif opsi == "3":
        umur_baru = input("Silahkan input umur baru: ")
        ubah(data_detail, "Umur", umur_baru)
    elif opsi == "4":
        alamat_baru = input("Silahkan input alamat baru: ")
        ubah(data_detail, "Alamat", alamat_baru)
    elif opsi == "5":
        print(f"Selamat Tinggal {data_detail['Nama']}")
        break
    else:
        print("Opsi tidak valid. Silahkan pilih opsi yang sesuai.")