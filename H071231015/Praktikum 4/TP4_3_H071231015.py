def maksimum(*daftar_angka):
    if not daftar_angka:
        print("Daftar kosong")

    angka_terbesar = daftar_angka[0]

    for i in range(len(daftar_angka)):
        if daftar_angka[i] > angka_terbesar:
            angka_terbesar = daftar_angka[i]

    print(angka_terbesar)

''' Test Case 1 '''
maksimum(1, 2, 4, 6, 9, 3, 1, 9, 10)

''' Test Case 2 '''
maksimum(0, 1, 90, 430, 23, 212, 34)
