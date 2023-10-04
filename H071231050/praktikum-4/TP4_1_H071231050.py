def stringpermutation(n) :
    try:
        huruf = n
        for i in range(len(n)):
            kata = huruf[-1] + huruf [:-1] 
            print(kata, end = " | ")
            huruf = kata
    except :
        print("invlaid data!")

n = input("masukkan kata : ")
stringpermutation(n)
