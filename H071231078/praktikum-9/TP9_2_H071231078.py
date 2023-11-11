class Mahasiswa:
    def __init__(self, Nama, Nim, Jurusan, Ipk):
        self.nama = Nama
        self.nim = Nim
        self.jurusan = Jurusan
        self.Ipk = Ipk

    def Tampilkan_info(self):
        info = "Nama Mahasiswa: " + self.nama + "\n" + "NIM: " + self.nim + "\n" + "Jurusan: " + self.jurusan + "\n" + "Nilai IPK: " + str(self.Ipk) + "\n"
        return info

    def Hitung_predikat(self):
        if self.Ipk >= 3.5:
            return "lulus dengan predikat cumlaude"
        elif self.Ipk >= 3.0:
            return "lulus dengan predikat sangat memuaskan"
        elif self.Ipk >= 2.5:
            return "lulus dengan predikat cukup"
        elif self.Ipk < 2.0:
            return "lulus dengan predikat kurang"

daftar_mahasiswa = []

while True:
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    jurusan = input("Masukkan Jurusan: ")
    ipk = float(input("Masukkan IPK: "))

    info_mahasiswa = Mahasiswa(nama, nim, jurusan, ipk)
    
    info = info_mahasiswa.Tampilkan_info()
    predikat = info_mahasiswa.Hitung_predikat()
    
    daftar_mahasiswa.append(info)
    daftar_mahasiswa.append(predikat)

    m = input("Apakah masih ingin melanjutkan (Y/N): ")
    if m == "N":
        break

# print(daftar_mahasiswa)
for i in range(0, len(daftar_mahasiswa),2):
    print(daftar_mahasiswa[i])
    print(daftar_mahasiswa[i+1])
    print(25*"-")

