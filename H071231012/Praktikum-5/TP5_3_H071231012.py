def anagram(kata1, kata2): #menerima 2 parameter
    return sorted(kata1.replace(" ","").lower()) == sorted(kata2.replace(" ","").lower())#mengurutkan kata secara alphabet

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")

if anagram(kata1, kata2):
    print(True)
else:
    print(False)
