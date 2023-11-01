import re
# tugs praktikum 8 nomor 2 
pattern1 = r"\b(25[0-5]|2[0-4][0-9]|[1]?[0-9]?[0-9])\b"
pattern2 = r"[A-Fa-f0-9]{1,4}:[A-Fa-f0-9]{1,4}:[A-Fa-f0-9]{1,4}:[A-Fa-f0-9]{1,4}:[A-Fa-f0-9]{1,4}:[A-Fa-f0-9]{1,4}:[A-Fa-f0-9]{1,4}:[A-Fa-f0-9]{1,4}"
c = []
a = int(input("masukkan IP address : "))
for i in range(a):
    b = input()
    n = re.findall(pattern1, b)
    m = re.findall(pattern2, b)
    if len(n) == 4:
        c.append("ipv4")
    elif len(m) == 1:
        c.append("ipv6")
    else:
        c.append("bukan ip address")

for i in c:
    print(i)