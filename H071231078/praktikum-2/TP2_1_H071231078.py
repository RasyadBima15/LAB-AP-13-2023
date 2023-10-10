print("pilih gender anda")
x = print("1. Pria ")
y = print("2. wanita")
x = 1
y = 2
z = int(input("= "))

if z == x:
      tb = float(input("masukkan tinggi badan : "))
      bb = float(input("masukkan berat badan : "))
      a = tb**2
      b = bb *10000
      bmi = b/a
      if bmi < 18 :
            print(f"anda tegolong underweight dengan BMI {bmi:.2f}")
      elif 23.99 >= bmi >= 18:
            print(f"anda tegolong normal dengan BMI {bmi:.2f}")
      elif 26.99 >= bmi >= 24:
            print(f"anda tegolong overwight dengan BMI {bmi:.2f}")
      elif bmi >= 27: 
            print(f"anda tegolong obese dengan BMI {bmi:.2f}")
elif z == y:
      tb = float(input("masukkan tinggi badan : "))
      bb = float(input("masukkan berat badan : "))
      a = tb**2
      b = bb *10000
      bmi = b/a
      if bmi < 17 :
            print(f"anda tegolong underweight dengan BMI {bmi:.2f}")
      elif 23.99 >= bmi >= 17:
            print(f"anda tegolong normal dengan BMI {bmi:.2f}")
      elif 27.99 >= bmi >= 24:
            print(f"anda tegolong overwight dengan BMI {bmi:.2f}")
      elif bmi >= 28: 
            print(f"anda tegolong obese dengan BMI {bmi:.2f}")