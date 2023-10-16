def campur(s1, s2):
    n = min( len(s1), len(s2)) #panjang kata minimum s1 dan s2
    s3 = " " #menampung hasil penggabungan
    for i in range(n):
        s3 += s1[i] + s2[-i-1]
    s3 += s1[n:] + s2[n:]
    return s3

print("Hasil mixed =", campur(input("s1 = "), input("s2 = ")))