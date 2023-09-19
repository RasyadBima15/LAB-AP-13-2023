# program menghitung berat badan idealyag dibedakan berdasarkan gendernya
print("\nData yang dimasukkan harus lebih dari 0")
# Input tinggi badan(cm) 
tinggi_badan = float(input('Masukan tinggi badan (cm) : ')) # harus > 0

# input berat badan (kg)
berat_badan = float(input('Masukan berat badan(kg) : ')) # harus > 0

if tinggi_badan <= 0 or berat_badan <= 0 :
    print("Mohon masukan data yang benar")
    exit()

tinggi_badan = tinggi_badan / 100

print("""Pilihlah gender Anda :
  1. Pria
  2. Wanita""")

bmi = berat_badan / (tinggi_badan **2)

pilihan_gender = input("Pilih gender Anda : ")

if pilihan_gender == "1" :
    print("1. Pria")
    if bmi < 18:
        kategori = "Underweight"
    elif 18 <= bmi < 24:
        kategori = "Normal"
    elif 24 <= bmi < 27:
        kategori = "Overweight"
    else:
        kategori = "Obese"

    #  penampilan hasil
    print(f"Anda terlihat {kategori} dengan BMI {bmi:.2f}")
    
elif pilihan_gender == "2":
    print("2. Wanita") 
    if bmi < 17:
        kategori = "Underweight"
    elif 17 <= bmi < 24:
        kategori = "Normal"
    elif 24 <= bmi < 28:
        kategori = "Overweight"
    else:
        kategori = "Obese"

    #  penampilan hasil
    print(f"Anda terlihat {kategori} dengan BMI {bmi:.2f}")

else :
    print("\nMohon memasukkan gender yang diakui oleh program (Pria/Wanita)")
    print("Coba lagi!")
    exit()

print("\nAkhir dari program\n")








    

