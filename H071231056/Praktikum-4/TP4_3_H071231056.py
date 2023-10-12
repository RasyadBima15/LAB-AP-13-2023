# nomor 3

def angka_maksimum_in_list(list):
    maksimum = list[0]
    for angka in list:
        if angka > maksimum:
            maksimum = angka
    return maksimum
list = list(map(int, input().split(" ")))
print(angka_maksimum_in_list(list))
