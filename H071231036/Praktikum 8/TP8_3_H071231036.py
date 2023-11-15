import re

def validasi_username(username):
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{5,20}$', username))

def validasi_email(email):
    return bool(re.match(r'^[a-z]+[a-z0-9]*@[a-z]+\.[a-z]{2,}(?:\.[a-z]{2,})?$', email))

def validasi_password(password):
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$', password))

username = input("Masukkan username: ")
email = input("Masukkan email: ")
password = input("Masukkan password: ")

if (
    validasi_username(username) and
    validasi_email(email) and
    validasi_password(password)
):
    print("Registrasi akun berhasil!")
else:
    print("Registrasi akun tidak valid. Silakan cek kembali input Anda.")
