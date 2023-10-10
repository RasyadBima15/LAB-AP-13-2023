#MENGHITUNG BMI

kelamin = input("jenis kelamin : \n1.laki-laki\n2.perempuan\nMasukkan pilihan : ")
tinggi = float (input("masukkan tinggi badan (cm) : "))
berat = float (input("masukkan berat badan (kg) : "))
tinggi_M = float (tinggi / 100)
BMI = float (f"{berat / (tinggi_M)**2:.2f}")

match kelamin :
    case "1" :
        if BMI < 18 :
            print (f"anda tergolong underweight dengan BMI {BMI}")
        elif 18 <= BMI < 24 :
            print (f"anda tergolong Normal dengan BMI {BMI}")
        elif 24 <= BMI < 27 :
            print (f"anda tergolong overweight dengan BMI {BMI}")
        else :
            print (f"anda tergolong obese dengan BMI {BMI}")
    case "2" :
        if BMI < 17 :
            print (f"anda tergolong underweight dengan BMI {BMI}")
        elif 17 <= BMI < 24 :
            print (f"anda tergolong Normal dengan BMI {BMI}")
        elif 24 <= BMI < 28 :
            print (f"anda tergolong overweight dengan BMI {BMI}")
        else :
            print (f"anda tergolong obese dengan BMI {BMI}")
    case _:
        print ("invalid data")

            
