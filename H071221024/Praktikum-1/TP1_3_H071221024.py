a = float(input("Input a = "))
b = float(input("Input b = "))
c = float(input("Input c = "))

x1 = (-b + (b * b - 4 * a * c) ** 0.5) / ( 2 * a)
x2 = (-b - (b * b - 4 * a * c) ** 0.5) / ( 2 * a)

print("x1 =", format(x1, ".2f"))
print("x2 =", format(x2, ".2f"))
