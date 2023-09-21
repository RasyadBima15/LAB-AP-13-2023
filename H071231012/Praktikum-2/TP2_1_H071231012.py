print ('pilih gender anda')
print ('1.Pria')
print ('2.Wanita')

gender = int (input ('masukkan gender= '))
berat = float(input('masukan berat badan : '))
Tinggi_badan = float(input('masukan tinggi badan anda : '))

tinggi = Tinggi_badan/100
bmi = (berat/(tinggi**2))

if gender == 1 :
    if bmi <18:
        print (f'Anda tergolong Underweight dengan BMI {bmi:.2f}')
    elif bmi >= 18 and  bmi <=23.9:
        print (f'Anda tergolong Normal dengan BMI {bmi:.2f}')
    elif bmi >=24 and bmi <26.9:
        print (f'Anda tergolong Overweight dengan BMI {bmi:.2f}')
    else :
        print (f'Anda tergolong Obese dengan BMI {bmi:.2f}')
elif gender == 2 :
    if bmi <17:
        print (f'Anda tergolong Underweight dengan BMI {bmi:.2f}')
    elif bmi >=17 and bmi <=23.9:
        print (f'Anda tergolong Normal dengan BMI {bmi:.2f}')
    elif bmi >=24 and bmi <=27.9: 
        print (f'Anda tergolong Overweight dengan BMI {bmi:.2f}')
    else :
        print (f'Anda tergolong Obese dengan BMI {bmi:.2f}')