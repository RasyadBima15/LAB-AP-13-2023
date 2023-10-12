# nomor 1

def permutasi_kata(n):

    for i in range(len(n)):
        m = n[1:] + n[:1]
        # print(n[:1])
        print(m, end="|")
        n = m

n = input()
permutasi_kata(n)


