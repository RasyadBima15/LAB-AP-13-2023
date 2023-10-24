gender=int(input("Pilih gender Anda\n1. Pria\n2. Wanita\n= "))

if gender != 1 and gender != 2:
    print("Pilih input yang valid")
else:
    tb = int(input("Masukkan tinggi badan (cm) : ")) / 100
    bb = int(input("Masukkan berat badan (kg) : "))
    bmi = bb / tb**2

    if gender == 1:
        if bmi < 18  :
            kategori = "kurus"
        elif 18 <= bmi < 24 :
            kategori = "Normal"
        elif 24 <= bmi < 27 :
            kategori = "Kegemukan"
        else:
            kategori = "Obesitas"
    else:
        if bmi < 17  :
            kategori = "kurus"
        elif 17 <= bmi < 24 :
            kategori = "Normal"
        elif 24 <= bmi < 28 :
            kategori = "kegemukan"
        else:
            kategori = "Obesitas"
 
print(f"Anda tergolong {kategori} dengan BMI {bmi:.2f}")
 


