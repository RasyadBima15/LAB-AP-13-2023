input1=input("Masukkan Input Pertama : ")
input2=input("Masukkan Input Kedua : ")
input3=input("Masukkan Input Ketiga : ")

match (input1, input2, input3):
    case ("vertebrado", "ave", "carnivoro"):
        print("aguia")
    case ("vertebrado", "ave", "onivoro"):
        print("pomba")
    case ("vertebrado", "mamifero", "onivoro"):
        print("homem")
    case ("vertebrado", "mamifero", "herbivoro"):
        print("vaca")
    case ("invertebrado", "inseto", "hematofago"):
        print("pulga")
    case ("invertebrado", "inseto", "herbivoro"):
        print("lagarta")
    case ("invertebrado", "anelideo", "hematofago"):
        print("sanguessuga")
    case ("invertebrado", "anelideo", "onivoro"):
        print("minhoca")
    case _:
        print("Invalid input")