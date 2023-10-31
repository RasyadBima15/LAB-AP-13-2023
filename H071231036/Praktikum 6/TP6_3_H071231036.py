try : 
    angka = list(map(int,input("Masukkan beberapa angka: ").split())) 

    angka_genap = []
    angka_ganjil = []
    angka_yang_habis_dibagi_5 = []

    for i in angka:
        if i % 2==0:
            angka_genap.append(i)
        else:
            angka_ganjil.append(i)
        if i % 5 == 0:
            angka_yang_habis_dibagi_5.append(i)
    print("Angka Ganjil: ", angka_ganjil)
    print("Angka Genap: ", angka_genap)
    print("Angka yang habis dibagi 5: ", angka_yang_habis_dibagi_5)
except : print ("inputan harus berupa integer")