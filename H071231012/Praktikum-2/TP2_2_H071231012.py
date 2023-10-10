pertama = input('masukkan inputan pertama : ')
kedua = input('masukkan inputan kedua : ')
ketiga = input('masukkan inputan ketiga : ')

match pertama : 
    case 'vertebrado' :
        if kedua == 'ave' :
            if ketiga == 'carnivoro' :
                print ('aguia')
            elif ketiga == 'onivoro' :
                print ('pomba')
            else :
                print ('invalid data')
        if kedua == 'mamifero' :
            if ketiga == 'onivoro' :
                print('homem')
            elif ketiga == 'herbivoro' :
                print ('vaca')
            else :
                print ('invalid data')
    case 'invertebrado' :
        if kedua == 'inseto' :
            if ketiga == 'hematofago' :
                print ('pulga')
            elif ketiga == 'herbivoro' :
                print ('lagarta')
            else :
                print ('invalid data')
        if kedua == 'anelideo' :
            if ketiga == 'hamatofago' :
                print('sanguessuga')
            elif ketiga == 'onivoro' :
                print ('minhoca')
            else :
                print ('invalid data')

    case _:
        print('Invalid Data')
       