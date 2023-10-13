def catAndMouse(catA, catB, mosC):
    dist_catA = abs(mosC - catA)  
    dist_catB = abs(mosC - catB)  
    
    if dist_catA < dist_catB:
        return "Cat A"
    elif dist_catB < dist_catA:
        return "Cat B"
    else:
        return "Mouse C"

result1 = catAndMouse(catA=16, catB=24, mosC=15)
print(result1)  

result2 = catAndMouse(catA=20, catB=10, mosC=15)
print(result2)  
