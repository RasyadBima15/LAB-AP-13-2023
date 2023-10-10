n = int(input('masukkan nilai = ')) 

if 0<= n: #supaya inputnya positif
    a, b = 0, 1
    count = 0 #suku

    while count< n: #perulangan
        print(a, end=' ') #print nilai a, diakhir diberikan spasi
        next_bil = a + b #suku berikutnya
        a = b
        b = next_bil
        count = count + 1
else:
    print('input tidak valid')