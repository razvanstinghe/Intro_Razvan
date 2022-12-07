# Flow control:  if, else
# evalueaza conditii si bifurca codul in functie de rezultat

# situatia if
piesa_faine = False
print('pornim radio')
if piesa_faine == True:
    print('dam mai tare')
    print('fredonez melodia')
print('oprim radio')

# situatia if, else

# if else
# daca nr este par, printam acest lucru
# altfel printam impar
nr = 4
if nr % 2 == 0:
    print('nr par')
else:
    print('impar')

# if, else if, else
# cum ne saluta robotelul in functie de ora
ora = int (input('introdu ora'))
if ora < 0:
    print('ora invalida')
elif ora <= 11:
    print("Buna dimineata")
elif ora <= 18:
    print('Buna ziua')
elif ora <= 21:
    print('Buna seara')
elif ora <= 24:
    print('Noapte buna')
else:
    print('ora invalida')