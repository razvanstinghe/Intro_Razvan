from clasa_2_tema_6 import Dreptunghi


a = int(input('Introdu valoarea lungimii: '))
b = int(input('Introdu valoarea latimii: '))
c = a * b
d = (2*a) + (2*b)
e = input('Introdu culoarea: ')
f = input('Introdu noua culoare a dreptunghiului: ')

rezultat = Dreptunghi(a, b, c, d, e, f)
rezultat.descriere_dreptunghi()
rezultat.aria_dreptunghi()
rezultat.perimetrul_dreptunghi()
rezultat.schimba_culoare()