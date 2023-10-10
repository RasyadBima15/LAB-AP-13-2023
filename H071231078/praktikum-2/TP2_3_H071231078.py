x = input("golongan =  ")
y = float(input("Daya =  "))
z = float(input("Pemakaian =  "))

golongan = ["R1","R2","R3","B2","B3","I3","P1"]

match x:
    case "R1":
        if 900 <= y < 1300:
            tagihan = z * 1352
            print(f"jumlah tagihan anda sebesar : Rp {tagihan:,.1f}". format(tagihan).replace(",", "_").replace(".", ",").replace("_", "."))
        elif 1300 <= y < 2200:
            tagihan = z * 1444.70
            print(f"jumlah tagihan anda sebesar : Rp {tagihan:,.1f}". format(tagihan).replace(",", "_").replace(".", ",").replace("_", "."))
        elif 2200 <= y < 3500:
            tagihan = z * 1444.70
            print(f"jumlah tagihan anda sebesar : Rp {tagihan:,.1f}". format(tagihan).replace(",", "_").replace(".", ",").replace("_", "."))
        else:
            print("data tidak valid")
    case "R2":
        if 3500 <= y <= 5500:
            tagihan = z * 1699.53
            print(f"jumlah tagihan anda sebesar : Rp {tagihan:,.1f}". format(tagihan).replace(",", "_").replace(".", ",").replace("_", "."))
        else:
            print("data tidak valid")
    case "R3":
        if y >= 6600:
            tagihan = z * 1699.53
            print(f"jumlah tagihan anda sebesar : Rp {tagihan:,.1f}". format(tagihan).replace(",", "_").replace(".", ",").replace("_", "."))
        else:
            print("data tidak valid")
    case "B2":
        if 6600 <= y <= 200000:
            tagihan = z * 1444.70
            print(f"jumlah tagihan anda sebesar : Rp {tagihan:,.1f}". format(tagihan).replace(",", "_").replace(".", ",").replace("_", "."))
        else:
            print("data tidak valid")
    case "B3":
        if y > 200000:
            tagihan = z * 1114.74
            print(f"jumlah tagihan anda sebesar : Rp {tagihan:,.1f}". format(tagihan).replace(",", "_").replace(".", ",").replace("_", "."))
        else:
            print("data tidak valid")
    case "I3":
        if y >= 200000:
            tagihan = z * 1314.12
            print(f"jumlah tagihan anda sebesar : Rp {tagihan:,.1f}". format(tagihan).replace(",", "_").replace(".", ",").replace("_", "."))
        else:
            print("data tidak valid")
    case "P1":
        if 6600 <= y <= 200000:
            tagihan = z * 1523.28
            print(f"jumlah tagihan anda sebesar : Rp {tagihan:,.1f}". format(tagihan).replace(",", "_").replace(".", ",").replace("_", "."))
        else:
            print("data tidak valid")
    case _:
        print("data tidak valid")