# tugas praktikum 8 nomor 1
import re
a = input("masukkan kata >> ")
if len(a) > 45:
    print("False")
else:
    b = re.findall(r"[A-Za-z02468]{40}[13579\s]{5}",a)
    print(b)
    if b: print("True")
    else: print("False")