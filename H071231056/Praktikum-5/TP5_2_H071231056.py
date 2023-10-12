def awalTengahAkhir(kata):
    berapa_kata = len(kata)

    if berapa_kata % 2 != 0:
        posisi = berapa_kata // 2
        tengah = kata[posisi]# ingat index mulai dari 0
    else:
        posisi = berapa_kata // 2
        tengah = kata[posisi - 1:posisi + 1]# ingat index mulai dari 0
        
    print(kata[0] + tengah + kata[-1])

kata = input("masukan kata : ")
awalTengahAkhir(kata)