a = float(input("input a : "))
b = float(input("input b : "))
c = float(input("input c : "))

x1 = (-b + (b**2 - 4*a*c)**0.5) /(2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5) /(2*a)

print("x1 = ", format(x1, ".2f") )
print("x2 = ", format(x2, ".2f") )