import math

a = float(input("input a : "))
b = float(input("input b : "))
c = float(input("input c : "))

x1 = -b + math.sqrt(b**2 - 4*a*c)
x2 = -b + - math.sqrt(b**2 - 4*a*c)

g = 2 * a

e = x1 / g
f = x2 / g

print(f"x1 = {e:.2f}")
print(f"x2 = {f:.2f}")