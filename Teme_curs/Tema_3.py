# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
print('rezolvare ex #1')
lista_note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
# ● Afișeaz-o
print(lista_note_muzicale)
# ● Inversează ordinea folosind slicing și suprascrie această listă.
lista_note_muzicale = lista_note_muzicale[::-1]
# ● Printează varianta actuală (inversată).
print(lista_note_muzicale)
# ● Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# deoarece metoda face asta automat.
lista_note_muzicale = lista_note_muzicale[::-1]
# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
# inițială.
# print(lista_note_muzicale2)
print(lista_note_muzicale)
# Concluzii: slicing e temporar, dacă vrei să păstrezi noua variantă va trebui să
# suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
# suprascrierea automat și permanentizează aceste modificări. Ambele variante
# își găsesc utilitatea în funcție de ce ne dorim în acel moment.

# 2. De câte ori apare ‘do’?
print('rezolvare ex #2')
print(lista_note_muzicale.count('do'))
# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
print('rezolvare ex #3')
lista_1 = [3, 1, 0, 2]
lista_2 = [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.
# varianta I
lista_unita = (lista_1 + lista_2)
print(lista_unita)
# varianta II
print(lista_1.__add__(lista_2))
# 4.● Sortează și afișază lista generată la exercițiul anterior.
print('rezolvare ex #4')

lista_unita = (lista_1 + lista_2)
lista_unita.remove(0)
print(sorted(lista_unita))
# ● Sortează numărul 0 folosind o funcție.

# ● Afișaza iar lista.
# 5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
print('rezolvare ex #5')
# ● Lista este goală.
if lista_unita == 0:
    print('Lista este goala')
# ● Lista nu este goală.
if lista_unita != 0:
    print('Lista NU este goala')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
print('rezolvare ex #6')
lista_noua = lista_unita.clear()
# 7. Copy paste la exercițiul 5. Verifică încă o dată.
print('rezolvare ex #7')
# Acum ar trebui să se afișeze că lista e goală.
print('valoare lista_noua: ', lista_noua)

# 8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print('rezolvare ex #8')
dict_1 = {
    "Ana": 8,
    "Gigel": 10,
    "Dorel": 5
}
# Folosește o funcție că să afișezi Elevii (cheile)
print(dict_1.keys())
# 9. Printează cei 3 elevi și notele lor
print('rezolvare ex #9')
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie
print('Ana a luat nota:', dict_1.get('Ana'), 'Gigel a luat nota:', dict_1.get('Gigel'), 'Dorel a luat nota:',
      dict_1.get('Dorel'))
# 10. Dorel a făcut contestație și a primit 6
print('rezolvare ex #10')
dict_1 = {
    "Ana": 8,
    "Gigel": 10,
    "Dorel": 6
}
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare
# print('Ana a luat nota:', dict_1.get('Ana'),'Gigel a luat nota:', dict_1.get('Gigel'), 'Dorel are noua nota:', dict_1.get('Dorel'))
print(f'Dorel are noua nota:', dict_1.get('Dorel'))
# 11. Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
dict_1.pop("Gigel")
print(dict_1)
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
dict_1.update({
    "Ionica": 9
})
# ● Printează noii elevi
print(dict_1)
# 12.
print('rezolvare ex #12')
# Set
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
# ● Adaugă în zilele_sapt ‘luni’
zilele_sapt = {'luni'}
# ● Afișeaza zile_sapt
print(zile_sapt)
# 13.Folosește un if și verifică dacă:
print('rezolvare ex #13')
# ● Weekend este un subset al zilelor din săptămânii.
if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor din săptămânii')
else:
    print('Weekend nu este un subset al zilelor din săptămânii')
# ● Weekend nu este un subset al zilelor din săptămânii.
# 14. Afișează diferențele dintre aceste 2 seturi.
print('rezolvare ex #14')
print(zile_sapt - weekend)
# 15. Afișază intersecția elementelor din aceste 2 seturi.
print('rezolvare ex #15')
print(zile_sapt.intersection(weekend))

# ---------EXERCITII OPTIONALE----------------------------------------------------
print('Rezolvare exercitii optionale')
# 1. Ne imaginăm o echipă de fotbal pt teren sintetic. 3 Schimbări maxime admise:
# ● Declară o Listă cu 5 jucători
# ● Schimbari_efectuate = te joci tu cu valori diferite
# schimbari_efectuate = int(input('Nr schimbari efectuate: '))
# ● Schimbari_max = 3
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# - Efectuează schimbarea
# - Șterge jucătorul scos din listă
# - Adaugă jucătorul intrat
# - Afișaza a intra x, a ieșit y, mai ai z schimbări
# Dacă jucătorul nu e în teren:
# - Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în teren
# - Afișază ‘mai ai z schimbări
# Testează codul cu diferite valori

echipa = ['Hagi', 'Petrescu', 'Popescu', 'Munteanu', 'Prunea']
print(echipa)
schimbari_efectuate = input('Introdu nr de schimbari efectuate: ')
schimbari_max = 3
x = int(schimbari_efectuate)
y = int(schimbari_max)
if x < y:
    i = input('Iese jucatorul: ')
else:
   print('Nu sunt disponibile schimbari!')
   exit()

if i in echipa:
    print('A iesit jucatorul: ' + i)
    echipa.remove(i)
    j = input("Intra jucatorul: ")
    echipa.append(j)
    print("A intrat jucatorul: " + j)
    if x == 0:
        print('Mai ai disponibile: ' + str('2') + ' schimbari.')
    else:
        print('Mai ai disponibile: ' + str(int(y - x)) + ' schimbari.')
else:
    print('Nu se poate efectua schimbarea, deoarece jucătorul' + ' ' + i + ' ' + 'nu este în teren.')


