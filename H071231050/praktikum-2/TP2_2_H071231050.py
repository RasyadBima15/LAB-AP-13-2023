#MEMBUAT PROGRAM YANG MENAMPUNG 3 INPUTAN

pilihan_pertama = input("masukkan input pertama : ")
pilihan_kedua = input("masukkan input kedua : ")
pilihan_ketiga = input("masukkan input ketiga : ")

match pilihan_pertama :
    case "vertebrado" :
        if pilihan_kedua == "ave" :
            if pilihan_ketiga == "carnivoro" :
                print("aguia")
            elif pilihan_ketiga == "onivoro" :
                print("pomba")
            else :
                print ("invalid data")
        elif pilihan_kedua == "mamifero" :
            if pilihan_ketiga == "onivoro" :
                print("homem")
            elif pilihan_ketiga == "herbivoro" :
                print("vaca")
            else :
                print ("invalid data")
        else :
            print ("invalid data")
    case "invertebrado" :
        if pilihan_kedua == "inseto" :
            if pilihan_ketiga == "hematofago" :
                print("pulga")
            elif pilihan_ketiga == "herbivoro" :
                print("lagarta")
            else :
                print ("invalid data")
        elif pilihan_kedua == "anelideo" :
            if pilihan_ketiga == "hematofago" :
                print("sanguessuga")
            elif pilihan_ketiga == "onivoro" :
                print("minhoca")
            else :
                print ("invalid data")
        else :
            print ("invalid data")
    case _:
        print("invalid data")
 