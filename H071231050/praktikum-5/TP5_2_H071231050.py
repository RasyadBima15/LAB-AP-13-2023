kata = input("masukkan kata : ")
hasil = len(kata)
if hasil < 3 :
    print('Inputan tidak boleh kurang dari 3 huruf')
elif hasil % 2 == 0 :
    hasil = kata [0] + kata[len(kata)//2-1] + kata[len(kata)//2] + kata[-1]
    print (hasil)
else : 
    hasil = kata [0] + kata[len(kata)//2-1] + kata[-1]
    print (hasil)