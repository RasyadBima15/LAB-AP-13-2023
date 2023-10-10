def tukar(kata):  
    if not isinstance(kata, str):
        raise TypeError("Input harus berupa string.")
    else:
        m = []
        for x in kata:
            m.append(x)
        print(m)
        for _ in range (len(m)):
            m.insert(0,m[-1])
            m.pop()
            print("".join(m), end=" | ")

n =(input())
print(f'stringPermutation("{n}")')
tukar(n)

# def tukar(n):
#     if not isinstance(n, str):    
#         raise TypeError("error")
#     else:
#         for i in range(1, len(n) + 1):
#             y = n[-i:] + n[:-i]
#             print(y, end=" | ")


# n = input()
# tukar(n)

