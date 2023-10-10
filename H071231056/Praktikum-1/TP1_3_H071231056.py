# Program untuk menghitung solusi persamaan kuadrat
'''dimana a, b, dan c sebagai inputan dan x sebagai output pada program'''
print ("\nMencari nilai x1 dan x2")
a = float(input("masukan nilai a = " )) # a != 0
if  a == 0 :
    print("NILAI a TIDAK BOLEH SAMA DENGAN 0 !!!")
    exit()# menghentikan program jika a = 0

else:

    b = float(input("masukan nilai b = " ))
    c = float(input("masukan nilai c = " ))

print("\njika nilai variabel a, b, dan c adalah",a,",",b,"dan", c,"maka :")

D = (b**2) - (4 * a * c)  # Menghitung diskriminan, agar ngak salah eksekusi(ngak pusing)

# if D < 0 :
#      print("penyelesaiannya bilangan complex")
# else:

# kalau maupake diatas(if else D ), janlupa dibawah dikasi spasi/ seleksi code dibawa , 
# lalu tekan Tab (bahwa itu bagian dari else:)
x1 = (-b + (D ** 0.5)) / (2 * a)
x2 = (-b - (D ** 0.5)) / (2 * a)


print(f"nilai x1 = {x1:.2f}")
print(f"nilai x2 = {x2:.2f}")

