def mouseAndCat(catA, catB, mosC):
    try :
        if abs(catA - mosC) < abs(catB - mosC):
            return "Cat A"
        elif abs(catA - mosC) > abs(catB - mosC):
            return "Cat B"
        elif abs(catA - mosC) == abs(catB - mosC):
            return "Mouse C"
    except :
        print ("Type error")
        
A = int(input('Masukkan posisi Cat A : '))
B = int(input('Masukkan posisi Cat B : '))
C = int(input('Masukkan posisi Mouse C : '))

output = mouseAndCat(A, B, C)
print(output)