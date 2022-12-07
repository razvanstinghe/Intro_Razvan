# listele in python pot sa cuprinda elemente de tipuri diferite
# si au dimensiune dinamica

fructe = ['mar', 'banana', 'portocala', 3, True, 3]

# afisam o lista
print(fructe)

# accesam un element in f de index
print(fructe[1])

# adaugam un nou element
fructe.append('rosie')

# suprascriem un element
fructe[0] = 'para'
print(fructe)

#dimensiunea
print(len(fructe))

# scoate si ne da returneaza ultimul element
last = fructe.pop()
print('ultimul element', last)
print('lista', fructe)

# de cate ori apare un element
print(fructe.count(3))

# extindem lista

fructe_exotice = ['ananas', 'kiwi']
fructe.extend(fructe_exotice)
print(fructe)