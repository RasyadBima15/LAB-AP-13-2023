import re

sentence = input("Masukkan String : ")
pattern = r"^[a-zA-Z02468]{40}[13579\s]{5}$"
status = re.search(pattern, sentence)

if status:
    print(True)
else:
    print(False)