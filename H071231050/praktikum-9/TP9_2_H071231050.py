class Mahasiswa:
    def __init__(self,nama,nim,jurusan,ipk) :
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkan_info(self) :
        print (f'Nama\t: {self.nama}')
        print (f'NIM\t: {self.nim}')
        print (f'Jurusan\t: {self.jurusan}')
        print (f'IPK\t: {self.ipk}')

    def hitung_predikat(self) :
        if self.ipk >= 3.5 :
            return "Cumlaude"
        elif self.ipk >= 3.0 :
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5 :
            return "Memuaskan"
        elif self.ipk >= 2.0 :
            return "Cukup"
        elif self.ipk < 2.0 :
            return "Kurang"

nama = input("Masukkan Nama Anda\t: ")
nim = input("Masukkan NIM Anda\t: ")
prodi = input("Masukkan Jurusan Anda\t: ")
ipk = float(input("Masukkan IPK Anda\t: "))

def biodata(nama,nim,prodi,ipk) :
    print("=" * 50)
    print("Biodata anda")
    print("=" * 50)
    informasi = Mahasiswa(nama,nim,prodi,ipk)
    informasi.tampilkan_info()
    print(f"Predikatnya {informasi.hitung_predikat()}")

biodata(nama,nim,prodi,ipk)
        

