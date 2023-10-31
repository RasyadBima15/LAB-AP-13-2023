def angka_kembar(arr1, arr2):
    return list(set(arr1) & set(arr2))

try :
    arr1 = list(map(int,input("Input array ke-1: ").split()))
    arr2 = list(map(int,input("Input array ke-2: ").split()))

    duplikat = angka_kembar(arr1, arr2)
    if len(duplikat)==1:
        print(f"Terdapat 1 buah duplikat yaitu ({duplikat[0]})")
    elif duplikat:
        print(f"Terdapat {len(duplikat)} buah duplikat yaitu {tuple(duplikat)}")
    else:
        print("Tidak ada duplikasi ditemukan.")
except :
    print("data harus berupa integer")
 