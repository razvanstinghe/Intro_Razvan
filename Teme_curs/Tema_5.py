#
print('Rezolvare #1')
# 1.Funcție care să calculeze și să returneze suma a două numere

a = int(input('Introdu primul numar: '))
b = int(input('Introdu al doilea numar: '))


def sum(numar1, numar2):
    total = numar1 + numar2
    return total
sum(a, b)


print(sum(a, b))

print('Rezolvare #2')

# 2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

de_introdus = int(input('Introdu nr pt a verifica daca este un nr par: '))

def este_par(numar_introdus):
    if de_introdus % 2 == 0:
        return print(True)
    else:
        return print(False)

este_par(de_introdus)

print('Rezolvare #3')
# 3. Funcție care returnează numărul total de caractere din numele tău complet.(nume, prenume, nume_mijlociu)

nume_complet = input('Introdu numele tau complet: ')

def count():
    for nr_caractere in nume_complet:
        nr_caractere == print(len(nume_complet) - nume_complet.count(' '))
        return nr_caractere

count()

print('Rezolvare #4')
# # 4. Funcție care returnează aria dreptunghiului

date_intrare1 = int(input('Introdu Lungimea dreptunghiului: '))
date_intrare2 = int(input('Introdu latimea dreptunghiului: '))

def multiplication(lungime, latime):
    arie_dreptunghi = date_intrare1 * date_intrare2
    return print(arie_dreptunghi)

multiplication(date_intrare1, date_intrare2)

print('Rezolvare #5')
# 5. Funcție care returnează aria cercului

date_intrare1 = int(input('Introdu valoarea razei cercului, stiindu-se deja ca valoarea lui Pi este constanta 3.14: '))
import math
math.pi

def multiplication(numar1, numar2):
    arie_cerc = numar2 * numar1*numar1
    return print(arie_cerc)

multiplication(date_intrare1, math.pi)

print('Rezolvare #6')
# 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.

afirmatie = input('Introdu un cuvant sau o propozitie scurta: ')
declaratie = input('Introdu o litera pentru a verifica daca exista in afirmatie: ')

def verifica_litera():
    for x in range(afirmatie.__contains__(declaratie)):
        return print(True)
    else:
        return print(False)

verifica_litera()

print('Rezolvare #7')
# 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y


def exe7():
    string = str(input("Introdu un string: "))
    counter_lower_case = 0
    counter_upper_case = 0
    for letter in string:
        if letter.islower():
            counter_lower_case +=1
        else:
            counter_upper_case +=1
    print("numarul de caractere mici este " + str(counter_lower_case))
    print("numarul de caractere mari este " + str(counter_upper_case))

exe7()

print('Rezolvare #8')
# 8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu numerele pozitive

input_lista = input('Introdu o lista de numere, pozitive si negative, separate prin spatiu: ').split()
num = 0

def lista_numere(pozitive):

    lista_pozitive = []

    for numar in pozitive:
        if int(numar) > 0:
            lista_pozitive.append(numar)

    return lista_pozitive

print(lista_numere(input_lista))

print('Rezolvare #9')
# 9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

x = int(input('Introdu primul numar: '))
y = int(input('Introdu al doilea numar: '))

def numere(numar1, numar2):

    if numar1 > numar2:
        print('Primul numar ' + str(x) + ' este mai mare decat al doilea numar ' + str(y))
    elif numar1 < numar2:
        print('Al doilea numar '+ ' ' + str(y) + ' ' +' este mai mare decat primul numar ' + ' ' + str(x))
    else:
        print('Numerele sunt egale')

numere(x, y)

print('Rezolvare #10')
# 10. Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ + returnează False


introdu_set = set(input('Introdu un set de numere despartite prin spatiu: ').split(' '))
numar_introdus = (input('Introdu numarul care trebuie adaugat in "set" : '))

def set_mare(set, numar):


    if set.__contains__(numar):
        print('Nu am adaugat numărul în set. Acesta există deja!')
        return print(False)

    else:
        print('Am adaugat numărul nou în set. ')
        return print(True)

set_mare(introdu_set, numar_introdus)


