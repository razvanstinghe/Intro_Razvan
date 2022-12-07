#------------FOR----------------
# propozitie = 'Ana are meRe.'
# for litera in propozitie :
#     # if litera == 'r' or litera == 'R':
#     # if litera == 'r' or litera == 'R':
#     if litera.upper() == 'R':
#         # print(propozitie[5])
#         print(litera)

#---------WHILE-------------
# index = 1
# while 25 >= index:
#     index += 1
#     print(index)
#     if index <= 25:
#         print('Maine este vineri.')
#         if index == 25:
#             break
#     # index += 1
#     print(index)
# else:
#     print('Am terminat de rulat')
#--------------------------------------
propozitie_2 = 'Ana are mere.'
for index in range(10):
     if index == 5:
        continue
     print(propozitie_2[index])
else:
    print('Am terminat')

#----------LISTA  IN  LISTA-----------
# paine = ['paine alba', 'paine Graaham', 'paine secara']
# lista_cumparaturi = ['lapte', 'oua', 'apa', ['creion', 'pix', 'radiera'], paine]
# for cumparatura in lista_cumparaturi:
#         # print('lista_cumparaturi') #face print de cate ori gaseste un produs => 4x
#         if type(cumparatura) == list:
#             cumparatura_clona = cumparatura
#             lista_cumparaturi.remove(cumparatura)
#             lista_cumparaturi.extend(cumparatura_clona)
#         print(type(cumparatura))
# print(lista_cumparaturi)
#             # for subprodus in produs:
#             #     print(subprodus)

# print(lista_cumparaturi)
# print(lista_cumparaturi[3])
# penar = lista_cumparaturi[3]
# pix = penar[1]
# print(lista_cumparaturi[3][1])
# print(lista_cumparaturi[4][2])

# varianta Andreea Torjoc:

# paine = ['paine alba', 'paine Graham', 'paine secara']
# lista_cumparaturi = ['lapte', 'oua', 'apa', ['creion', 'pix', 'radiera'], paine]
# lista_cumparaturi2 = []
# for produs in lista_cumparaturi:
#     if type(produs) == list:
#         for subprodus in produs:
#             print(subprodus)
#             lista_cumparaturi2.append(subprodus)
#     else:
#         #print(produs)
#         lista_cumparaturi2.append(produs)
# print(lista_cumparaturi2)

# FOR EACH se parcurge o lista sau un string
# vezi while vs for

# EXERCITII:
# def - reprezinta cuvantul "cheie" pentru o functie





