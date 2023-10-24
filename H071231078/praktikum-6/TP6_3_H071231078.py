a = list(map(int,input().split()))
angkaGanjil, angkaGenap, angkaKelipatanLima = [],[],[]

for i in a:
    if i % 2 == 0: angkaGenap.append(i)
    if i % 2 != 0: angkaGanjil.append(i)
    if i % 5 == 0: angkaKelipatanLima.append(i)

print(f"""Angka Genap  : {angkaGenap}
angka Ganjil : {angkaGanjil}
Angka yang habis dibagi 5 : {angkaKelipatanLima} """)