import re

while True:
    try:
        N = int(input("Jumlah IP Address yang ingin dicek : "))
        break
    except:
        print(f"\nMohon masukkan angka")

total_N = []
for i in range(N):
    total_N.append(input())

pattern_IPv4 = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
pattern_IPv6 = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'

for n in total_N:
    if re.findall(pattern_IPv4,n):
        print("IPv4")
    elif re.findall(pattern_IPv6,n):
        print("IPv6")
    else:
        print("Bukan IP Address")