def sort(x):
    for i in range(len(x)): 
        for y in range(len(x)-i-1):
            if x[y] > x[y+1]:
                a = x[y]
                x[y] = x[y+1]
                x[y+1] = a
    
                
angka = list(map(int,input().split(",")))
sort(angka)
print(f"maksimum{tuple(angka)}")
print(">>",angka[-1])
