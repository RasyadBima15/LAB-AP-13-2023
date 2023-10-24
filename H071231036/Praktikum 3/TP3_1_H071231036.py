n = int(input("Masukkan jumlah suku Fibonacci yang ingin dijumlahkan: "))

a, b = 0, 1

if n <= 0:
    print("Tidak ada suku Fibonacci yang dijumlahkan.")
elif n == 1:
    print("0")
else:
    print(a, b, end=" ")

    for _ in range(n - 2):
        a, b = b, a + b
        print(b, end=" ")
