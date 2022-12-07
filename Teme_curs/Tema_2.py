# 1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if else.
# folosim "if" atunci cand dorim sa verificam o functie indeplineste anumite conditii, iar atunci cand acele
# conditii nu sunt indeplinite, programul va rula situatia "else".

# 2. Verifică și afișează dacă x este număr natural sau nu.
print('exercitiul #2:')
x = 2
if x > 0:
    print(x)
    print('conditia de la #2 este indeplinita')
else:
    print('=> conditia de la #2 nu este indeplinita')

# 3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
print('exercitiul #3:')
if x > 0:
    print('x este nr pozitiv')
if x < 0:
    print('x este nr negativ')
if x == 0:
    print('x este nr neutru')

# 4. Verifică și afișează dacă x este între -2 și 13.
print('exercitiul #4:')
if x >= -2 and x <= 13:
    print('conditia de la #4 este indeplinita')

# 5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
print('exercitiul #5:')
x = 2
y = 3
if x - y < 5:
    print('conditia de la #5 este indeplinita')

# 6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
print('exercitiul #6:')
if not (x > 5 and x < 27):
    print('Conditia este indeplinita.')

# 7. x și y (int). Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
print('exercitiul #7:')
x = 2
y = 3
if x == y:
    print('x = y')
else:
    print(max(x,y))

# 8. X, y, z - laturile unui triunghi. Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
print('exercitiul #8:')

x = input('Latura x are lungimea: ')
y = input('Latura y are lungimea: ')
z = input('Latura z are lungimea: ')
if x == y == z:
    print('triunghi echilateral')
elif (x == y or x == z or y == z):
    print('triunghi isoscel')
else:
    print('triunghi oarecare')

# 9. Citește o literă de la tastatură. Verifică și afișează dacă este vocală sau nu
print('exercitiul #9:')
litera = input('Introdu litera pentru verificare: ')
if litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u':
    print('"litera" este vocala')
else:
    print('"litera" este consoana')

# 10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
print('exercitiul #10:')
nota = input('Introdu nota elevului: ')
if nota >= str('9'):
    print('nota este: A')
elif nota >= str('8') and nota < str('9'):
    print('nota este: B')
elif nota >= str('7') and nota < str('8'):
    print('nota este: C')
elif nota >= str('6') and nota < str('7'):
    print('nota este: D')
elif nota >= str('4') and nota < str('6'):
    print('nota este: E')
elif nota < str('4'):
    print('nota este: F')

# Exercitii optionale:

# 1.Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
print('Ex #1 optional')
x1 = 7895
if (len(str(x1)) >= 4):
    print('x1 are minim 4 cifre')
x2 = 10
if(len(str(x2)) <= 2):
    print('x2 nu are minim 4 cifre')

# 2.Verifică dacă x are exact 6 cifre.
print('Ex #2 optional')
if (len(str(x1)) == 6):
    print('x1 are exact 6 cifre')
else:
    print('afirmatia este falsa')
# 3.Verifică dacă x este număr par sau impar (x e int).
# print('Ex #3 optional')
# X = input('Valoarea lui X este: ')
# if (X%2 == 0):
#     print('nr este par')
# else:
#     print('nr este impar')
# 4. x, y, z (int). Afișează care este cel mai mare dintre ele?
print('Ex #4 optional')
x = 2
y = 3
z = 5
print(max('x', 'y', 'z'))

# 5.X, y, z - reprezintă unghiurile unui triunghi. Verifică și afișează dacă triunghiul este valid sau nu.
print('Ex #5 optional')

a = input('Unghiul lui x este: ')
b = input('Unghiul lui y este: ')
c = input('Unghiul lui z este: ')

if (a + b + c) != 180:
     print('Triunghiul este valid.')
else:
     print('Triunghiul NU este valid.')

# 6. Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# ● Citiți de la tastatură un int x
# ● Afișează stringul fără ultimele x caractere
# Exemplu: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'
print('Ex #6 optional')
x = 'Coral is either the stupidest animal or the smartest rock'
print(len(x))
y = 3
print(x[0:-y])

# 7.Același string. Declară un string nou care să fie format din primele 5 caractere + ultimele 5
print('Ex #7 optional')
x2 = 'Coral is either the stupidest animal or the smartest rock'
y = x2[0:5]
z = x2[52:]
print(y,z)

# 8. Același string.
print('Ex #8 optional')
# ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
# este o funcție care te ajuta sa faci asta)
x2 = 'Coral is either the stupidest animal or the smartest rock'
print(str.index(x2, 'rock'))
# ● Folosind această variabilă + slicing, afișează tot stringul până la acest cuvant
# ● output: 'Coral is either the stupidest animal or the smartest '
print(x2[0:53])



# 10. Avand stringul '0123456789'
print('Ex #10 optional')
c = '0123456789'
# ● Afișați doar numerele pare
print(c[2:9:2])
# ● Afișați doar numerele impare
# (hint: folositi slicing, controlați din pas)
print((c[1:9:2]))

# 9. Citește de la tastatura un string
print('Ex #9 optional')
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atentie: se dorește ca programul sa fie case insensitive - 'apA' e acceptat
x3 = 'perioada'
a = x3[0:1]
b = x3[7]
print(a)
print(b)
assert (a == b)
