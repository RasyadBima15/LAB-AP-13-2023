kata = input(f'Masukkan kata : ').replace(' ','')
huruf_tengah = len(kata)//2
if len(kata) < 3:
    print("Invalid input, harus minimal 3 huruf")
else:
    if len(kata) % 2 == 0:
        print(kata[0] + kata[huruf_tengah -1] + kata[huruf_tengah] + kata[-1])
    else:
        print(kata[0] + kata[huruf_tengah] + kata[-1])
        