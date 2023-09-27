tagihan = int(input('Masukkan jumlah yang ingin dibayar : '))
pembayaran = int(input('Masukkan nilai uang anda : '))
kembalian = pembayaran - tagihan

uang = [100000,50000,20000,10000,5000,2000,1000]
jumlah = 0
if kembalian <= 0 :
    print ("uang anda tidak cukup")
else :
    for pecahan in uang :
        jumlah = kembalian // pecahan
        kembalian = kembalian % pecahan
        print (f'{jumlah} uang pecahan Rp,{pecahan:,}'.replace(',','x').replace('.',',').replace('x','.'))
