# soal nomor 2
# memasukan tiga inputan

a = input("\nMasukan Input Pertama : ")
if a == "vertebrado":
    b = input("Masukan Input Kedua   : ")
    if b == "ave" :
        c = input("Masukan Input Ketiga  : ")
        if c == "carnifora" :
            print("agula")
        elif c == "onivoro":
            print("pomba")

    elif b == "mamifero":
        c = input("Masukan Input Ketiga  : ")
        if c == "onivoro" :
            print("homem")
        elif c == "herbivoro":
            print("vaca")

if  a == "invertebrado":
    b = input("Masukan Input Kedua   : ")
    if b == "inseto" :
        c = input("Masukan Input Ketiga  : ")
        if c == "hematofago" :
            print("pulga")
        elif c == "herbivoro":
            print("lagarta")
        
    
    elif b == "anelideo":
        c = input("Masukan Input Ketiga  : ")
        if c == "hematofago" :
            print("sanguessuga")
        elif c == "onivoro":
            print("minhoca")
        
        else: # agar invalid kalau salah input di ke 3
            print("\nInvalid Input")
            print("\nCoba lagi!\n")
            exit()
    else:
        print("\nInvalid Input")
        print("\nCoba lagi!\n")
        exit()

else:
    print("\nInvalid Input")
    print("\nCoba lagi!\n")
    exit()

print("\nAkhir dari program\n")

# ALTERNATIF

# a = input("\nMasukkan Input Pertama : ")
# b = input("Masukkan Input Kedua   : ")
# c = input("Masukkan Input Ketiga  : ")

# match (a, b, c):
#     case ("vertebrado", "ave", "carnivora"):
#         print("aguia")
#     case ("vertebrado", "ave", "onivoro"):
#         print("pomba")
#     case ("vertebrado", "mamifero", "onivoro"):
#         print("homem")
#     case ("vertebrado", "mamifero", "herbivoro"):
#         print("vaca")
#     case ("invertebrado", "inseto", "hematofago"):
#         print("pulga")
#     case ("invertebrado", "inseto", "herbivoro"):
#         print("lagarta")
#     case ("invertebrado", "anelideo", "hematofago"):
#         print("sanguessuga")
#     case ("invertebrado", "anelideo", "onivoro"):
#         print("minhoca")
#     case _:
#         print("\nInvalid Input")
#         print("\nCoba lagi!\n")
#         exit()

# print("\nAkhir dari program\n")



