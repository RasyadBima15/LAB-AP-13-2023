import re
import os

class Data:
    def __init__(self, nama, email, password):
        self.nama = nama
        self.email = email
        self.password = password

    @classmethod
    def create_data(cls):
        while True:
            nama = input("Masukkan Nama: ")
            email = input("Masukkan Email: ")

            while True:
                if not re.match(r"[a-z0-9]+@student.unhas.ac.id$", email) or \
                        any(char in email for char in ['_', '/', '-']) or \
                        any(char.isupper() for char in email) or \
                        any(char.isspace() for char in email):
                    print(45*"=")
                    print("Email yang Anda Masukkan Salah")
                    print(45*"=")
                    email = input("Masukkan Email: ")   
                else:
                    break

            password = input("Masukkan Password: ")

            while True:
                if not (8 <= len(password) <= 20) :
                        print(45*"=")
                        print("Password harus memiliki panjang 8-20")
                        print(45*"=")
                        password = input("Masukkan Password: ")
                else:
                    if not any(char.isupper() for char in password) or \
                        not any(char.islower() for char in password) or \
                        not any(char.isdigit() for char in password):
                        print(45*"=")
                        print("Password yang anda masukkan tidak sesuai syarat")
                        print(45*"=")
                        password = input("Masukkan Password: ")
                    else:
                        break

            return cls(nama, email, password)

    
    def show_detail():
        if not data_list:
            print(45*"=")
            print("Data saat ini kosong")
            print(45*"=")
        else:
            print(45*"=")
            print("Data Anda Adalah")
            for data in data_list:
                print("Nama:", data.nama)
                print("Email:", data.email)
                print("Password:", data.password)
            print(45*"=")

    def change_name():
        if not data_list:
            print(45*"=")
            print("Data saat ini kosong.")
            print(45*"=")
        else:
            print(45*"=")
            nama_baru = input("Masukkan Nama Baru: ")
            for data in data_list:
                data.nama = nama_baru
            print(45*"=")

    def save_data_to_file():
        if not data_list:
            print(45*"=")
            print("Data saat ini kosong.")
            print(45*"=")
        else:
            print(45*"=")
            file_name = input("Silahkan Masukkan Nama File : ")
            file_name += ".txt"
            
            if not os.path.exists(file_name):
                with open(file_name, 'w') as file:
                    file.write(45*"="+"\n")
                    file.write("Data Yang Tersimpan\n")
                    file.write(45*"="+"\n")
                    for data in data_list:
                        file.write(f"Nama: {data.nama}\n")
                        file.write(f"Email: {data.email}\n")
                        file.write(f"Password: {data.password}\n")
                        file.write(45*"="+"\n")
            else:
                with open(file_name, 'a') as file:
                    for data in data_list:
                        file.write(f"Nama: {data.nama}\n")
                        file.write(f"Email: {data.email}\n")
                        file.write(f"Password: {data.password}\n")
                        file.write(45*"="+"\n")

            
            print("Berhasil")
            data_list.clear()
            print(45*"=")

    def count_data_in_file():
        print(45*"=")
        file_name = input("Silahkan Masukkan Nama File : ")
        file_name += ".txt"

        if not os.path.exists(file_name):
            print(f"Tidak Terdapat File dengan Nama {file_name}")
            print(f"jumlah data pada file : 0")
        else:
            with open(file_name, 'r') as file:
                data_content = file.read()
                data_count = data_content.count("Nama:")
                print(f"Jumlah Data pada File {file_name}: {data_count}")
        
        print(45*"=")

data_list = []

print(45*"=")
while True:
    print("selamat datang dan silahkan pilih opsi anda")
    print("a. Detail Anda\nb. Ubah nama\nc. Jumalah Data Pada File\nd. Save Data pada File\ne. Buat Data Baru\nf. Keluar ")
    opsi = input("silahkan pilih opsi : ")

    if opsi == 'a':
        Data.show_detail()
    elif opsi == 'b':
        Data.change_name()
    elif opsi == 'c':
        Data.count_data_in_file()
    elif opsi == 'd':
        Data.save_data_to_file()
    elif opsi == 'e':
        new_data = Data.create_data()
        data_list.append(new_data)
        print(45*"=")
        print("Data berhasil dibuat!")
        print(45*"=")
    elif opsi == 'f':
        print("Sampai Jumpa Lagi")
        break
    else:
        print("Opsi tidak valid. Silakan pilih opsi yang benar.")

        








