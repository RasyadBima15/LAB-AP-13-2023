def catAndMouse(catA, catB, mosC):
    jarak_A = abs(catA - mosC)
    jarak_B = abs(catB - mosC)
    if jarak_A < jarak_B:
        print('Cat A')
    elif jarak_A > jarak_B:
        print('Cat B')
    else:
        print('Mouse C')

''' Test Case 1 '''
catAndMouse(catA = -24, catB = 24, mosC = 15)

''' Test Case 2 '''
catAndMouse(catA = 20, catB = 10, mosC = 15)