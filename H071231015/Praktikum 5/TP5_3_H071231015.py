kata_1 = input(f'Masukkan kata pertama: ').replace(" ","").lower()
kata_2 = input(f'Masukkan kata kedua: ').replace(" ","").lower()

if len(kata_1) == len(kata_2):
    daftar_1 = []
    daftar_2 = []

    for huruf in kata_1:
        daftar_1.append(huruf)
    for huruf in kata_2:
        daftar_2.append(huruf)

    hasil = True

    for i in daftar_1:
        if i not in daftar_2:
            hasil = False
            break

    if hasil:
        print(True)
    else:
        print(False)
else:
    print(False)

# Versi pendek :
# kata_1 = input('Masukkan kata pertama: ').replace(" ", "").lower()
# kata_2 = input('Masukkan kata kedua: ').replace(" ", "").lower()
# anagram = len(kata_1) == len(kata_2) and sorted(kata_1) == sorted(kata_2)
# print(anagram)