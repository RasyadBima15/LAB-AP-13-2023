import re

def validasi(input_str):
    if len(input_str) != 45:
        return False
    
    if not re.match("^[a-zA-Z02468]{40}$", input_str[:40]):
        return False
    
    if not re.match("^[13579\s]{5}$", input_str[40:]):
        return False
    
    return True

input_str = input("Masukkan string: ")
result = validasi(input_str)

if result:
    print("True")
else:
    print("False")
