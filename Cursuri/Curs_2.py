# a = 5
# print(a)
# a += 3 + a
# a = a+3+a # reprezentare linie 3
# print(a)
# if a == 22:
#     print('am ajuns aici')
# elif a == 29:
#         print('Aici e 29')
# else:
#     print(('Am ajuns aici in else'))

# qwer = 'taste'
# if qwer.__contains__('as'):
#    qwer += '123'
#    print('Exista')
#    print(qwer[5])
#    print(type(qwer[5]))
#
#    if int(qwer[5]) == 1:
#         print('Exista nr')

# variabila = 40
# if variabila in range(30, 50):
#     numar = str(variabila) + ' ani' # cu numar = str(variabila) se converteste din int in string
#     print(numar)
#     if numar.__contains__(' '):
#         print('Corect')
#     if numar.find(' '):
#         print('corect corect')

pret = 678
if pret >= 678:
    elev = 'Ionel a luat nota 6'
    # print(len(elev))
    nota = elev[:17:-1]
    print(nota)
    print(type(nota))
    nota = float(nota)
    if nota >= 4.5:
        print('Ai trecut')
# print(a[:len(a)-2:-1])
# sau asa:
# elev = 'Ionel a luat nota 6'
#     nota = len(elev[::-1])
#     if nota >= 4.5:
#         print ('ai trecut')
