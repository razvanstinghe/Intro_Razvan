print('Rezolvare #1')
# 1.Având lista:

# Folosește un for că să iterezi prin toată lista și să afișezi;
# ● ‘Mașina mea preferată este x’.
# ● Fă același lucru cu un for each.
# ● Fă același lucru cu un while.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
m = 0
for m in range(len(masini)):
    print(f'Masina mea preferata este: {masini[m]}')

for masina in masini:
    print(f'Masina mea preferata este {masina}')

masina = len(masini)
m = 0
while m < masina:
    print(f'Masina mea preferata este {masini[m]}')
    m += 1

print('Rezolvare #2')
# 2. Aceeași listă:
# Folosește un for else
# În for
# - Modifică elementele din listă astfel încât să fie scrie cu majuscule,
# exceptând primul și ultimul.
# În else:
# - Printează lista.

masini1 = []
index = 0
for elem in masini:
    if index != 0 and index != len(masini)-1:
        masini1.append((elem.upper()))
    else:
        masini1.append(elem)
    index += 1
else:
    print(masini1)


print('Rezolvare #3')
# 3. Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Itereaza prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
# Printează ‘am găsit mașina dorită de dvs’
# Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
# Printează ‘Am găsit mașina X. Mai căutam‘

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Mercedes':
        print(f'Am găsit mașina dorită de dvs. este Mercedes.')
        break
    else:
        print(f'Am gasit masina {masina}.Mai cautam.')


print('Rezolvare #4')
# 4. Aceași listă;
# Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
# excepția Trabant și Lăstun.
# - Dacă mașina e Trabant sau Lăstun:
# Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
# else).
# - Printează S-ar putea să vă placă mașina x.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == "Trabant" or masina == "Lăstun":
        continue
    print(f'S-ar putea sa va placa masina {masina}')

print('Rezolvare #5')
# 5. Modernizează parcul de mașini:
# ● Crează o listă goală, masini_vechi.
# ● Itereaza prin mașini.
# ● Când găsesti Lăstun sau Trabant:
# - Salvează aceste mașini în masini_vechi.
# - Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# ● Printează Modele vechi: x.
# ● Modele noi: x.

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for masina in masini:
    if masina == "Trabant" or masina == "Lăstun":
        masini_vechi.append(masina)
        idx = masini.index(masina)
        masini[idx] = 'Tesla'
print(f'Modele vechi : {masini_vechi}')
print(f'Modele noi: {masini}')

print('Rezolvare #6')
# 6. Având dict:
# Vine un client cu un buget de 15000 euro.
# ● Prezintă doar mașinile care se încadrează în acest buget.
# ● Itereaza prin dict.items() și accesează mașina și prețul.
# ● Printează Pentru un buget de sub 15000 euro puteți alege mașină
# xLastun
# ● Iterează prin listă.




pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
masini_buget = []
for key, value in pret_masini.items():
    if value < 15000:
        print(f'Pentru buget de 15000 euro, puteti alege masina {key}')
        print(masini_buget.extend({key}))
        # print(masini_buget)
for elem in masini_buget:
    print("Masinile care se incadreaza in acest buget sunt:" + elem)

print('Rezolvare #7')
# 7. Având lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# ● Iterează prin ea.
# ● Afișează de câte ori apare 3 (nu ai voie să folosești count).
# print(numere)

lista_3 = []
for value in numere:
    if value == 3:
        lista_3.append(value)
        print(f"am gasit 3 de {len(lista_3)} ori")

print('Rezolvare #8')
# 8. Aceeași listă:
# ● Iterează prin ea
# ● Calculează și afișează suma numerelor (nu ai voie să folosești sum).

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
i = 0
for n in numere:
    i += n
print(i)

print('Rezolvare #9')
# 9. Aceeași listă:
# ● Iterează prin ea.
# ● Afișază cel mai mare număr (nu ai voie să folosești max).
# max = numere[3]
# print(max)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
i = 0
for n in numere:
    if i <= n:
        i = n
print(i)

# 10. Aceeași listă:
# ● Iterează prin ea.
# ● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# ● Afișază noua listă.

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numere_inversate = []
for n in numere:
    if n > 0:
        numere_inversate.append(-n)
    else:
        numere_inversate.append(n)
print(numere_inversate)
