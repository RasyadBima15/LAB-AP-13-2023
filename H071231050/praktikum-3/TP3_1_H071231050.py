angka = int (input("masukkan nilai : "))
if angka > 0:
    a = 0
    b = 1
    for i in range (angka) :
        print (a, end=" ")
        a, b = b , a + b
else :
    print ("invalid")

    
