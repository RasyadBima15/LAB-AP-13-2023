class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def Tampilkan_info(self):
        print(f"\nNama Mahasiswa : {self.nama}")
        print(f"NIM : {self.nim}")
        print(f"Jurusan : {self.jurusan}")
        print(f"IPK : {self.ipk}")

    def Hitung_predikat(self):
        if self.ipk >= 3.5:
            print("Cumlaude")
        elif self.ipk >= 3.0:
            print("Sangat Memuaskan")
        elif self.ipk >= 2.0:
            print("Cukup")
        else:
            print("Kurang")



def pilih(Nama, Nim, Jurusan, Ipk):
    var = Mahasiswa(Nama, Nim, Jurusan, Ipk)
    while True:
        print(f"\nPilih opsi :\n1. Tampilkan info\n2. Predikat\n3. Keluar")
        opsi = input("Masukkan pilihan : ")
        if opsi == '1' or opsi == '2' or opsi == '3':
            if opsi == '1':
                var.Tampilkan_info()
                pilih(Nama, Nim, Jurusan, Ipk)
            elif opsi == '2':
                var.Hitung_predikat()
                pilih(Nama, Nim, Jurusan, Ipk)
            else:
                exit()
        else:
            print("Mohon pilih antara 1, 2 atau 3")

Nama = input("Masukkan nama : ")
Nim = input("Masukkan NIM : ")
Jurusan = input("Masukkan jurusan : ")
while True:
    try:
        Ipk = float(input("Masukkan ipk : "))
        break
    except:
        print("Mohon masukkan angka desimal ")

pilih(Nama, Nim, Jurusan, Ipk)