def generate_permutasi(word):
   
    word = str(word)
    permutasi = []
    for i in range(1, len(word)):
        word = word[-1] + word[:-1]
        permutasi.append(word)

    hasil_permutasi = '|'.join(permutasi)
    print(hasil_permutasi)

input_word = input("Masukkan kata: ")
generate_permutasi(input_word)
