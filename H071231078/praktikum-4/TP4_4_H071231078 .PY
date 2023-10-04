def catAndMouse(catA,catB,mouseC):
    jarak_kucing1 = abs(catA - mouseC)
    jarak_kucing2 = abs(catB - mouseC)
    
    if jarak_kucing1 == jarak_kucing2:
        print("MouseC")
    elif jarak_kucing1 > jarak_kucing2:
        print("CatB")
    elif jarak_kucing2 > jarak_kucing1:
        print("CatA")

l = int(input())
m = int(input())
n = int(input()) 
print(f"catAndMouse(CatA = {l}, CatB = {m}, mouseC = {n})")
catAndMouse(l,m,n)


