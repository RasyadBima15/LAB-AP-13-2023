# nomor 4

def CatAndMouse(cat_A,Cat_B,mouse):
    #  ketika posisi kedua kucing tersebut sama terhadap tikus
     if abs(cat_A-mouse) == abs(Cat_B-mouse):
        return "Mouse C"
    #  ketika posisi kucing a lebih dekat dari kucing b
     elif abs(cat_A-mouse) < abs(Cat_B-mouse):
         return "Cat A"
    #  return cat b
     return "Cat B"

cat_A = int(input())
Cat_B = int(input())
mouse = int(input())

print(CatAndMouse(cat_A,Cat_B,mouse))