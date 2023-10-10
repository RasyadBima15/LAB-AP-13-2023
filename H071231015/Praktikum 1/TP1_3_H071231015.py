print(f'Mesin Persamaan Kuadrat')
a = float(input("Input a = "))
if a == 0:
    print("Nilai a tidak boleh sama dengan 0")
    exit()
else:
    b = float(input("Input b = "))
    c = float(input("Input c = "))

D = (b**2) - 4*a*c

if D > 0:
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    print('x1 = ' + format(x1,'.2f'))
    print('x2 = ' + format(x2,'.2f'))
elif D == 0:
    x = -b / (2*a)
    print('x = ' + format(x,'.2f'))
else:
    print(f'Tidak memiliki solusi')