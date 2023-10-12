def tambah_kata(kata1, kata2):
    hasil = ""
    panjang_kata1 = len(kata1)
    panjang_kata2 = len(kata2)

    for i in range(max(panjang_kata1, panjang_kata2)):#menangani jika ada kata yang lebih panjang
        if i < panjang_kata1:
            hasil += kata1[i]
        if i < panjang_kata2:# buat lebih mudah
            hasil += kata2[panjang_kata2 - 1 - i]

    return hasil

kata1 = "abcdefg"
kata2 = "XYZQW"
print(tambah_kata(kata1, kata2))