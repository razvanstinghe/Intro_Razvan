def verifica_prezenta():  # modul in care definim o functie
    lista = ['Ionel', 'Gicu', 'Popescu']  # declaram o lista
    for index in range(3):  # sau: for index in range(len(lista)-1):
        print(lista[index])
    # assert lista[index] == 'Ionel'

verifica_prezenta()

# ------------------------------------
# string_masini = input('Scrie o lista de masini, despartite cu ,: ')
# print(string_masini)
# lista_masini = string_masini.split(',')


# def returneaza_litera(portocala, mar = 5):  # print(lista_masini)
#     print(mar)
#     for masina in portocala:  # for each
#         if masina == 'Tractor':
#             for indexlitera in range(len(masina)):  # s-a modificat "litera" in "indexlitera" pt ca
#                 if masina[indexlitera] == 'b':
#                     return (masina[indexlitera])
#                 elif masina[indexlitera] == 't':
#                          return (masina[indexlitera])
#
#
# print(returneaza_litera(lista_masini, 8))  # reprezinta "call" la functie
# list1 = [0,1,2,3]
# list2 = [0,1,4,5]
# lista3 = list1 + list2
# print(list(set(lista3))) # merguire lista1 cu lista2 in lista3 si fara duplicate(!!!)

# index = 0
# while index < 5:
#     list1 = [0,1,2,3,4]
#     print(list1[index])
#     index = index + 1  #din cauza ca 5 nu se afla in lista si ca index = index + 1 => eroare : list out of range
