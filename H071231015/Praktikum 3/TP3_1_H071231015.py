n = int(input())
if n <= 0:
    print("Input tidak valid")
else:
    deret1 = 0
    deret2 = 1
    for _ in range(n):
        print(deret1, end=" ")
        deret3 = deret1 + deret2
        deret1 = deret2
        deret2 = deret3
        
