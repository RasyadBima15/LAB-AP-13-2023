kata = input("Masukan kata: ")

if len(kata) >=3: 
    if len(kata)%2 ==1:
        kata2 = kata[0] + kata[len(kata)//2] + kata[-1]
        print (kata2)
    if len(kata)%2 ==0:
        kata2 = kata[0] + kata[len(kata)//2-1] + kata[len(kata)//2] + kata[-1]
        print (kata2)
else :
    print ("Anda memasukan kata yang salah")