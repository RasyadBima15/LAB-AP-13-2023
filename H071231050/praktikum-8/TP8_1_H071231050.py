import re
pattern = r'^[A-Za-z02468]{40}[13579 ]{5}$'
# text = "x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo1395779"
# text = "2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57"
text = input("Masukkan kata : ")
result = re.match (pattern, text)
if result :
    print("True")
else :
    print("False")