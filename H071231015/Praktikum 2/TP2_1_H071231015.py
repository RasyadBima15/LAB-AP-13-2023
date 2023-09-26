print('Pilih Gender Anda')
print('1. Pria')
print('2. Wanita')
gender = int(input(f'= '))
if gender == 1 or gender == 2:
    tinggi = float(input(f'Masukkan tinggi badan (cm) : '))
    berat = float(input(f'Masukkan berat badan (kg) : '))
else:
    print(f'Harap masukkan angka 1 atau 2')
    exit()

bmi = ((berat)/(tinggi ** 2)) * 10000

if gender == 1:
    if bmi < 18:
        status = 'Underweight'
    elif 18 <= bmi <= 23.9:
        status = 'Normal'
    elif 24 <= bmi <= 26.9:
        status = 'Overweight'
    else:
        status = 'Obese'
elif gender == 2:
    if bmi < 17:
        status = 'Underweight'
    elif 17 <= bmi <= 23.9:
        status = 'Normal'
    elif 24 <= bmi <= 27.9:
        status = 'Overweight'
    else:
        status = 'Obese'

print(f'Anda tergolong {status} dengan BMI {bmi:.2f}')