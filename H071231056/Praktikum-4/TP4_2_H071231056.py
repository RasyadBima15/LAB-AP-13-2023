# nomor 2

def apakahPolindrom(word = str) -> str:
        hilangkan_spasi = word.replace(" ","").lower()
        if hilangkan_spasi == hilangkan_spasi[::-1]:
            return "polindrom"
        else:
            return "bukan polindrom"
word=input()  
print(apakahPolindrom(word))
