# tugas praktikum 8 nomor 3
import re

# head
def is_valid_username(username):
    pattern = r'^[A-Za-z\d]{5,20}$'
    return re.search(pattern, username)

def is_valid_email(email):
    pattern = r"^[a-z]+[0-9]{2,}@[a-z]+\.(com|co\.id)$"
    return re.search(pattern, email)

def is_valid_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$"
    return re.search(pattern, password)

# body
username = input("Masukkan username: ")
if is_valid_username(username):
    email = input("Masukkan email: ")
    if is_valid_email(email):
        password = input("Masukkan password: ")
        if is_valid_password(password):
            print("\nRegistrasi berhasil! ...") 
            print(f"Halo {username}")
        else:
            print("\nPassword yang kamu input tidak valid. Registrasi gagal.")
    else:
        print("\nEmail yang kamu input tidak valid. Registrasi gagal!")
else:
    print("\nInputan username tidak valid. Registrasi")