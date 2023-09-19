# program untuk menginput informasi daya listrik dan menghitung total tagihan
# input datannya
Golongan = input("Golongan = ")

if Golongan == "R1":# karean R1 ada 3 jadi saya gabungaja
    Daya =float(input("Daya = "))
    if Daya == 900:
        tagihan =  1352
    elif Daya == 1300:
        tagihan =  1444.70
    elif Daya == 2200:
        tagihan = 1444.70  
    else:
        print("data tidak valid")
        exit()

elif Golongan == "R2":
    Daya =float(input("Daya = "))
    if 3500 <= Daya <= 5500:
        tagihan = 1699.53
    else:
        print("data tidak valid")
        exit()

elif Golongan == "R3":
    Daya =float(input("Daya = "))
    if Daya >= 6600:
        tagihan = 1699.53
    else:
        print("data tidak valid")
        exit()

elif Golongan == "B2":
    Daya =float(input("Daya = "))
    if 6600 <= Daya <= 200000:# 200 kVA x 1000 = 200000 VA
        tagihan = 1444.70
    else:
        print("data tidak valid")
        exit()

elif Golongan == "B3":
    Daya =float(input("Daya = "))
    if Daya >= 200000:
        tagihan = 1114.74
    else:
        print("data tidak valid")
        exit()

elif Golongan == "I3":
    Daya =float(input("Daya = "))
    if Daya >= 200000 :
        tagihan = 1314.12
    else:
        print("data tidak valid")
        exit()

elif Golongan == "P1":
    Daya =float(input("Daya = "))
    if 6.600 <= Daya <= 200000:
        tagihan = 1523.28
        
    else:
        print("data tidak valid")
        exit()
else:
    print("data tidak valid")
    exit()

Pemakaian = float(input("Pemakaian = "))
total_tagihan = tagihan * Pemakaian
print(f"Jumlah tagihan anda sebesar : Rp, {total_tagihan:,.2f}".replace(",","x").replace(".",",").replace("x","."))
    
