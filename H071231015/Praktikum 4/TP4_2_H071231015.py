def palindrom(kata: str) -> str:
    kata = kata.replace(' ', '').lower()
    panjang_kata = len(kata)
    
    for i in range(panjang_kata // 2):
        if kata[i] != kata[panjang_kata - i - 1]:
            return print("Bukan palindrom")
    return print("Palindrom")

''' Test Case 1 '''
palindrom("Kasur ini rusak")

''' Test Case 2 '''
palindrom("Step on no pets")
