# Nomor 1
alas = float (input ("masukkan nilai alas :"))
tinggi = float (input ("masukkan nilai tnggi :")) 
garis_miring = float (tinggi**2 + alas**2)**(1/2)  #menggunakan yanda "()" pada angka 1/2 agar saat di run dia mengerjakannya terlebih dahulu  

rumus_luas = (1/2 * alas * tinggi)
luas = (rumus_luas)
rumus_keliling = (alas + tinggi + garis_miring)
keliling = (rumus_keliling)
print (f'luas = {rumus_luas:.2f}cm^2')   #menggunakan round agar angka dibelakang koma terbatas
print (f'keliling = {rumus_keliling:.2f}cm')   #menggunakan round agar angka dibelakang koma terbatas