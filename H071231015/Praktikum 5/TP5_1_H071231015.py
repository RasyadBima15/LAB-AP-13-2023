s1 = input(f's1 = ').replace(" ","")
s2 = input(f's2 = ').replace(" ","")[::-1]
s3 = ''

i = 0
while i < len(s1) and i < len(s2):
    s3 += s1[i] + s2[i]
    i += 1
s3 += s1[i:] + s2[i:]

print(f'Hasil mixed = "{s3}"')