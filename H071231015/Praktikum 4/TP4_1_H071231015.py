def stringPermutation(kata):
    try:
        if len(kata) <= 1:
            return print(kata)

        hasil_permutasi = []
        for i in range(len(kata)):
            kata = kata[-1:] + kata[:-1]  
            hasil_permutasi.append(kata)

        return print(' | '.join(hasil_permutasi) + ' |')

    except TypeError as msg:
        return print(f'Terjadi kesalahan karena {msg}')

''' Test Case 1 '''
stringPermutation("Kasur")

''' Test Case 2 '''
stringPermutation("Ayam")