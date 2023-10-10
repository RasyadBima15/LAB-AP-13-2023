# tugas praktikum 1
def mixed_string(a,b):
    c = "".join(reversed(b))
    m = ""
    if len(a) < len(b):
        for i in range(len(a)):
            m += a[i] + c[i]

        f = b[:-len(a)]
        g = "".join(reversed(f))
        m += g
        print(m)
    else:
        for i in range(len(b)):
            m += a[i] + c[i]

        f = a[len(b):]
        g = "".join(reversed(f))
        m+=g
        print(m)

m = input()
n = input()
mixed_string(m,n)