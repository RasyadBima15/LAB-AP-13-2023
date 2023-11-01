import re
input_string = input("Masukkan user: ")
pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'
if re.findall(pattern, input_string) and len(input_string) == 45:
    print(True)
else:
    print(False)