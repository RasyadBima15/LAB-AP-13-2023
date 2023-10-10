#tugas praktikum 3
def anagram(a,b):
    m = a.replace(" ","")
    n = b.replace(" ","")
    c = []
    d = []

    for char in m: c.append(char)
    for char in n: d.append(char)

    kata1 = [x.upper() for x in c]
    kata2 = [x.upper() for x in d]

    e = sorted(kata1)
    f = sorted(kata2)

    print(e)
    print(f)

    if e == f: print("True")
    else: print("False")

a = input()
b = input()
anagram(a,b)