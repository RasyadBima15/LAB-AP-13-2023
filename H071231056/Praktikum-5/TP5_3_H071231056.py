def anagram(kata1, kata2):
    kata1 = sorted(kata1.replace(" ", "").lower())
    kata2 = sorted(kata2.replace(" ", "").lower())
    
    if kata1 == kata2:
        print("True")
    else:
        print("False")

kata1 = "Astronomer"
kata2 = "Moon Starer"
anagram(kata1, kata2)