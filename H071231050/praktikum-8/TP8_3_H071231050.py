import re
def TesUsername(username):
    pattern = r"^[A-Za-z0-9]{5,20}$" 
    return re.match(pattern, username)
def TesEmail(email):
    pattern = r"^[a-z]+[0-9]{2,}@[a-z]+\.(com|co\.id)"
    return re.match(pattern, email)
def TesPassword(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    return re.match(pattern, password)

username = input("Masukkan username : ")
if TesUsername(username):
    email = input("Masukkan email : ")
    if TesEmail(email):
        password = input("Masukkan password : ")
        if TesPassword(password):
            print(f"\nRegistrasi berhasil! Halo {username}")
        else:
            print("\nPassword yang kamu input beresiko dihack. Registrasi gagal.")
    else:
        print("\nEmail yang kamu input tidak valid. Registrasi gagal!")
else:
    print("\nInputan username tidak valid dalam sistem. Registrasi gagal!")