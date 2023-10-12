# program untuk menentukan jenis karakter dari inputan dengan manipulasi string(isX methode)
print("\nmenentukan jenis karakter")
print(25*"_")
karakter = input("masukan karakter : ")
apakah_kapital = karakter.isupper() 
# hasilnya boolean, karna is, maka dibawa kita casting jadi sting(str)
'''kenapa? karean kita akan mencetaknya bersama string yaitu 
"Apakah huruf Kapital?", "Apakah huruf kecil?" dan "Apakah angka?"
karna mereka itu sudah string. ketika kita cetak string dan nilai boolean bakal terjadi kesalahan,
kalau tanpa apakah apakah itu, bisa!, ngkak perlu di konversi ke string(str)'''

print("Apakah huruf kapital? " + str(apakah_kapital))# diconverssi dulu ke str
apakah_kecil = karakter.islower()
print("Apakah huruf kecil? "+ str(apakah_kecil))# diconverssi dulu ke str
apakah_angka = karakter.isdecimal()
print("Apakah angka? "+ str(apakah_angka))# diconverssi dulu ke str



