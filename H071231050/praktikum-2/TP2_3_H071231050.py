#MENGHITUNG JUMLAH TAGIHAN
  

golongan_anda = input ("golongan = ")
daya_va = float (input ("daya = "))
pemakaian = float (input ("pemakaian = "))



match golongan_anda :
    case "R1" :
        if daya_va == 900 :
            tagihan = pemakaian * 1352
            print (f'jumlah tagihan anda sebesar : Rp, {tagihan:,}'.replace(',','x').replace('.',',').replace('x','.'))
        elif daya_va == 1300 :
            tagihan = pemakaian * 1444.70
            print (f'jumlah tagihan anda sebesar : Rp, {tagihan:,}'.replace(',','x').replace('.',',').replace('x','.'))
        elif daya_va == 2200 :
            tagihan = pemakaian * 1444.70
            print (f'jumlah tagihan anda sebesar : Rp, {tagihan:,}'.replace(',','x').replace('.',',').replace('x','.'))
        else :
            print ("data tidak valid")
    case "R2" :
        if daya_va <= 5500 and daya_va >= 3500 :
            tagihan = pemakaian * 1699.53
            print (f'jumlah tagihan anda sebesar : Rp, {tagihan:,}'.replace(',','x').replace('.',',').replace('x','.'))
        else :
            print ("data tidak valid")
    case "R3" :
        if daya_va >= 6600 :
            tagihan = pemakaian * 1699.53
            print (f'jumlah tagihan anda sebesar : Rp, {tagihan:,}'.replace(',','x').replace('.',',').replace('x','.'))
        else :
            print ("data tidak valid")
    case "B2" :
        if daya_va <= 200000 and daya_va >= 6600 :
            tagihan = pemakaian * 1444.70
            print (f'jumlah tagihan anda sebesar : Rp, {tagihan:,}'.replace(',','x').replace('.',',').replace('x','.'))
        else :
            print ("data tidak valid")
    case "B3" :
        if daya_va >= 200000 :
            tagihan = pemakaian * 1114.74
            print (f'jumlah tagihan anda sebesar : Rp, {tagihan:,}'.replace(',','x').replace('.',',').replace('x','.'))
        else :
            print ("data tidak valid")
    case "I3" :
        if daya_va >= 200000 :
            tagihan = pemakaian * 1314.12
            print (f'jumlah tagihan anda sebesar : Rp, {tagihan:,.2f}'.replace(',','x').replace('.',',').replace('x','.'))
        else :
            print ("data tidak valid")
    case "P1" :
        if daya_va <= 200000 and daya_va >= 6600 :
            tagihan = pemakaian * 1523.28
            print (f'jumlah tagihan anda sebesar : Rp, {tagihan:,}'.replace(',','x').replace('.',',').replace('x','.'))
        else :
            print ("data tidak valid")
    case _:
        print ("invalid data")



            










