# 1. Ce este o variabila de tip string
#  o variabila de tip string este o variabila
# 3. variabila string

telefon = 'iPhone'
model = '12'
magazin = 'Emag - magazin online'
stoc = 'Stocul este de (buc):'
nr_buc = '10'
pret = '2250.503'
moneda = "RON"
stoc_suficient = True
status_stoc = 'Stoc suficient: '

print(f'{status_stoc}{stoc_suficient}')
print(f'Oferta: {telefon} {model}. Se poate cumpara de la: {magazin} cu pretul de: {pret} {moneda}.')
print(f'{stoc} {nr_buc}.')

for i in range(1, 20, 3):
    print(f'{i}' )
