# FUNCTII - reprezinta niste functii de bloc
# functia ajuta la acel moment in care nu vrem sa repetam acel cod
# functia simpla nu primeste paramtri, doar executa cod ex: print('Am inceput tema')

import math
a = 5
b = 3
d = 10
def hi():
    print("am inceput tema!")
def sum(numar1, numar2, numar4):
    numar3 = numar1 + numar2 + numar4
    return numar3
    sum(a+b+d)
hi()
print(sum(a,b,d))
