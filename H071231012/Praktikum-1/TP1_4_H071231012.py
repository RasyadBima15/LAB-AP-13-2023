print("pengujian jenis karakter")
print("-"*20)
karakter = input("karakter = ")


huruf_kapital = karakter.isupper()
huruf_kecil = karakter.islower()
angka = karakter.isnumeric()

print("huruf kapital? " + str(huruf_kapital))
print("huruf kecil? " + str(huruf_kecil))
print("angka? " + str(angka))