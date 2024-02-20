import os
import re

simpan = [] 

class Menu:
    def __init__(self, Name, Email, Password):
        self.Name = Name
        self.Email = Email
        self.Password = Password

    def Detail_Anda(self):
        print("Data anda adalah")
        print(f"Nama     : {self.Name}\nEmail    : {self.Email}\nPassword : {self.Password}\n{'='*100}")

    def Ubah_Nama(self, Name):
        simpan.pop(0)
        self.Name = Name
        simpan.insert(0, self.Name)        

    def Ubah_Email(self, Email):
        simpan.pop(1)
        self.Email = Email
        simpan.insert(1,self.Email)

    def Ubah_Password(self, Password):
        simpan.pop(2)
        self.Password = Password
        simpan.insert(2, self.Password)

    def Buat_Data_Baru(self):
        simpan.append(self.Name)
        simpan.append(self.Email)
        simpan.append(self.Password)


class Save(Menu):
    def __init__(self, Name, Email, Password):
        super().__init__(Name, Email, Password)

    def file_pertama(self, nama_file):
        with open(f"File Data/{nama_file}.txt", "w") as file:
            file.write(f"+{'='*99}\n|Data yang tersimpan\n+{'='*99}")

    def isi_file(self, nama_file):
        with open(f"File Data/{nama_file}.txt", "a") as file:
            file.write(f"\n|Nama          : {self.Name}")
            file.write(f"\n|Email         : {self.Email}")
            file.write(f"\n|Password      : {self.Password}")
            file.write(f"\n+{'='*99}")
        print(f"Berhasil\n{'='*100}")
       
    def simpan_file(self, Name, Email, Password):
        cek = True
        while True:
            if cek == False:
                break
            else:
                nama_file = input('Silahkan masukkan nama file : ')
                print('='*100)
                folder_path = "File Data"
                if not os.path.exists(f"{folder_path}"):
                    os.mkdir(f"{folder_path}")

                if os.path.exists(f"File Data/{nama_file}.txt"):
                    print(f"File {nama_file}.txt sudah ada")
                    while True:
                        print(f"Pilih opsi:\n1. Gabung file\n2. Ganti nama")
                        opsi_file = input("Masukkan pilihan : ")
                        if opsi_file == '1' or opsi_file == '2':
                            if opsi_file == '1':
                                var.isi_file(nama_file)
                                # var.file_pertama(nama_file)
                                cek = False
                                simpan = []
                                # simpan.clear()
                                break
                            elif opsi_file == '2':
                                var.simpan_file(Name, Email, Password)
                                cek = False
                                simpan = []
                                # simpan.clear()
                                break
                        else:
                            print("Mohon masukkan 1 atau 2")
                else:
                
                    var.file_pertama(nama_file)
                    var.isi_file(nama_file)
                    # simpan.clear()
                    break
                    
    

def cek_email():
    while True:
                email = input("Silahkan masukkan email Anda    : ")
                pattern = r"(?=.*[a-z])(?=.*\d)"
                if re.findall(pattern, email):
                    pattern = r"^[a-z0-9]+@student.unhas.ac.id$"
                    if re.findall(pattern, email):
                        break
                    else:
                        print(f"{'='*100}\nMohon gunakan email yang terdaftar di SSO Unhas (@student.unhas.ac.id)\n{'='*100}")        
                else:
                    print(f"{'='*100}\nEmail harus mengandung minimal 1 huruf kecil dan 1 angka\n{'='*100}")
    return email


def cek_pw():
    while True:
                pw = input("Silahkan masukkan password Anda : ")
                pattern = r"^[a-zA-Z0-9]{8,20}"
                if re.findall(pattern, pw):
                    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,20}$"
                    if re.findall(pattern, pw):
                        print('='*100)
                        break
                    else:
                        print(f"{'='*100}\nPassword yang anda masukkan terlalu lemah\nGunakan minimal 1 huruf kapital, huruf kecil, dan angka\n{'='*100}")
                else:
                    print(f"{'='*100}\nPassword harus memiliki panjang 8-20\n{'='*100}")
    return pw



''' Program Utama '''


print(f"{'='*100}\n|{'SELAMAT DATANG DI TUPRAK 10'.center(98)}|\n{'='*100}")
while True:
    print(f"Silahkan pilih opsi menu Anda\n1. Detail Anda\n2. Ubah data\n3. Jumlah data pada file\n4. Save data pada file\n5. Buat data baru\n6. Keluar\n{'='*100}")
    opsi = input("Silahkan pilih opsi Anda : ")
    print('='*100)
    ans = ['1','2','3','4','5','6']
    if opsi in ans:

        if opsi == '1':
            if simpan == []:
                print(f"Data saat ini kosong\n{'='*100}")
            else:
                var.Detail_Anda()

        elif opsi == '2':
            if simpan == []:
                print(f"Data saat ini kosong\n{'='*100}")
            else:
                while True:
                    print(f"1. Ubah nama\n2. Ubah email\n3. Ubah Password\n4. Kembali")
                    pilih = input(f"Masukkan opsi : ")
                    print('='*100)
                    if pilih == '1' or pilih == '2' or pilih == '3' or pilih == '4':
                        if pilih == '1':
                            nama_baru = input('Silahkan input nama baru      : ')
                            var.Ubah_Nama(nama_baru)
                            break
                        elif pilih == '2':
                            email_baru = cek_email()
                            var.Ubah_Email(email_baru)
                            break
                        elif pilih == '3':
                            password_baru = cek_pw()
                            var.Ubah_Password(password_baru)
                            break
                        else:
                            break
                    else:
                        print("Mohon pilih antara 1, 2, 3 atau 4")
                print('='*100)
                    

        elif opsi == '3':
            nama_file = input('Silahkan masukkan nama file : ')
            if not os.path.exists(f"File Data/{nama_file}.txt"):
                print(f"Tidak terdapat file dengan nama {nama_file}.txt")
                print(f"Jumlah data pada file       : 0 data\n{'='*100}")
            else:
                with open(f"File Data/{nama_file}.txt", "r") as file:
                    Jumlah = file.read().count("Nama")
                print(f"Jumlah data pada file       : {Jumlah} data\n{'='*100}")

        elif opsi == '4':
            if simpan == []:
                print(f"Data saat ini kosong\n{'='*100}")
            else:
                var = Save(simpan[0], simpan[1], simpan[2])
                var.simpan_file(simpan[0], simpan[1], simpan[2])
                simpan.clear()


        elif opsi == '5':
            if simpan != []:
                while True:
                    tanya = input("Data Anda sudah ada. Tetap ingin buat baru? (ya/tidak) : ").lower()
                    if tanya == 'ya':
                        nama = input("Silahkan masukkan nama Anda     : ")
                        email = cek_email()
                        pw = cek_pw()
                        var = Menu(nama, email, pw)
                        var.Buat_Data_Baru()
                        break
                    elif tanya == 'tidak':
                        print('='*100)
                        break
                    else:
                        print("Mohon pilih ya/tidak")
                        print('='*100)
            else:
                nama = input("Silahkan masukkan nama Anda     : ")
                email = cek_email()
                pw = cek_pw()
                var = Menu(nama, email, pw)
                var.Buat_Data_Baru()

                
        else:
            print(f"{'='*100}\n|{'TUPRAK 10 SELESAI'.center(98)}|\n{'='*100}")
            exit()
    else:
        print(f"Mohon masukkan pilihan opsi yang benar\n{'='*100}")