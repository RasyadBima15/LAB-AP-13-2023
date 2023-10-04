def maksimum(*indeks):
    try:
        hasil_max = indeks[0]
        for angka in indeks:
            if angka >= hasil_max:
                hasil_max = angka
        return hasil_max

    except:
        print("Error")
print(maksimum(67,1,3,4,5,6,7,8,9,10,11,2))
