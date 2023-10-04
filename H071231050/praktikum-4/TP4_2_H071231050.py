def kata(n: str) -> str:
    try :
        bacaan = n.upper()
        print(bacaan)
        if bacaan != bacaan[::-1]:
            return "Bukan Palindrom"
        else:
            return "Palindrom"
    except :
        print("Type Error")

n = input("Masukkan sebuah kata: ")
hasil = kata(n)
print(f"'{n}' adalah {hasil}")
