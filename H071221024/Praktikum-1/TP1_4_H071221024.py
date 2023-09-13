print("Pengujian jenis karakter")
print("-"*25)

karakter = input("Karakter = ")

hurufKapital = karakter >= 'A' and karakter <= 'Z'
hurufKecil = karakter >= 'a' and karakter <= 'z'
angka = karakter >= '0' and karakter <= '9'

print("Huruf kapital?", hurufKapital)
print("Huruf kecil? ", hurufKecil)
print("Angka? ", angka)