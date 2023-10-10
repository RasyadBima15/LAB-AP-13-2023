kata1 = input("Masukkan kata pertama : ").lower().replace(' ','')
kata2 = input("Masukkan kata kedua : ").lower().replace(' ','')
error = 0
for i in kata1:
    status1 = kata1.count(i)
    status2 = kata2.count(i)
    if status1 != status2 :
        error += 1
if error == 0 and len(kata1) == len(kata2) :
    print ("True")
else:
    print ("False")