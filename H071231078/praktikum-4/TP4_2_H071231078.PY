# tugas 2 praktikum
def palindrome(kata:str):
    kata = [] 
    for char in n:
        kata.append(char)

    kata = [x.upper() for x in kata]

    y = list(kata)
    y.reverse()
    print(y)
    print(kata)

    if y == kata:
        print("palindrome")
    else:
        print("bukan palindrome")

n = input()
print(f'palindrome("{n}")')
palindrome(n)