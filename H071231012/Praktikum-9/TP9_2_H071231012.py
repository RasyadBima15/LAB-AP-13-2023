class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkan_info(self):
        print("Nama     :", self.nama)
        print("NIM      :", self.nim)
        print("Jurusan  :", self.jurusan)
        print("IPK      :", self.ipk)

    def hitung_predikat(self):
        if self.ipk >= 3.5:
            return "Cumlaude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Cukup"
        else:
            return "Kurang"

# Contoh penggunaan
nama = input("Nama     : ")
nim = input("NIM      : ")
jurusan = input("Jurusan  : ")
ipk = float(input("Ipk      : "))
print("="*50)

mahasiswa1 = Mahasiswa(nama, nim, jurusan, ipk)

mahasiswa1.tampilkan_info()
print("Predikat :", mahasiswa1.hitung_predikat())
print("="*50)