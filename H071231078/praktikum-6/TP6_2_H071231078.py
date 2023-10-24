a = set(map(int,input().split()))
b = set(map(int,input().split()))
c = tuple(a & b)
if len(c) > 0: 
    print(f"terdapat {len(c)} buah duplikat yaitu {c} ")
else:
    print("tidak ada duplikasi ditemukan")