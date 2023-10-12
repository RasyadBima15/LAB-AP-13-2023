print("\n\t\t\t\tProgram menghasilakan suku fibonacci\n".upper())
n = int(input("Masukkan deret suku Fibonacci yang diinginkan : "))

if n <=0:
    print("n >= 1")

a = 0
b = 1
    
for i in range(n):
    print(a, end =" ")
    bilangan = a + b
    a = b
    b = bilangan 
   
