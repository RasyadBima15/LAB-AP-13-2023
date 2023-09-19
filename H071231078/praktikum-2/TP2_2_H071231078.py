x = input("masukkan inputan pertama : ")
y = input("masukkan inputan kedua : ")
z = input("masukkan inputan ketiga : ")

a = "vertebrado"
b = "invertebrado"
c = "ave"
d = "mamifero"
e = "carnivoro"
f = "onivoro"
g = "herbivoro"
h = "inseto"
i = "anelideo"
j = "hematofago"

if x == a:
      if y == c:
        if z == e:
            print("aguia")
        elif z == f:
            print("pomba")
      elif y == d:
        if z == f:
            print("homem")
        elif z == g:
            print("vaca")
elif x == b:
      if y == h:
        if z == j:
            print("pulga")
        elif z == g:
            print("lagarta")
      elif y == i:
        if z == j:
            print("sanguessuga")
        elif z == f:
            print("minhoca")
