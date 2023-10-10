# tugas praktikum 2
def char_fml(a):
    if len(a) > 2:
        if len(a) % 2 == 0:   
            b = int((len(a))/2)
            c = a[0],a[b-1],a[b],a[-1]
            print("".join(c))
        else:
            b = int(1+(len(a))/2)
            c = a[0],a[b-1],a[-1]
            print("".join(c))
    else:
        print("error")

a = input()
char_fml(a)