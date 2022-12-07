# TEMA 1

# o variabila reprezinta un sir de caractere sub forma de combinatii de litere, cifre, simboluri, stocate in memorie
# variabilele au nume unic,

# STRING
fruct = 'mar'
print(type(fruct)) # => se verifica tipul de date
print('1. Acesta este un ' + fruct + '.')

# INT
nr_buc_kg = 6
print(type(nr_buc_kg)) # => se verifica tipul de date
m = str(nr_buc_kg) # am transformat din INT in STRING pentru a putea concatena (forma o propozitie)
print('2. Intr-un kg intra aproximativ ' + m + ' bucati.') # printare propozitie

# FLOAT
pret_RON_kg = 5.25
print(type(pret_RON_kg)) # => se verifica tipul de date
print(pret_RON_kg.__round__()) # aplicare rotunjire
print(type(pret_RON_kg.__round__())) # => se verifica tipul de date, => INT
n = str(pret_RON_kg)
print('3. Pretul de ' + n + ' RON/kg este fix.')

# BOOLEAN
produs_disponibil = False
print(type(produs_disponibil)) # => se verifica tipul de date
l = str(produs_disponibil)
print('4. Produsul este in stoc: ' + l)

nume = 'Stinghe'
prenume = 'Razvan'
print((len(nume)) + len(prenume))
s = str(len(nume) + len(prenume))
print('Numele complet are ' + s + ' caractere.')
print(nume + ' ' + prenume + ' ' + s + ' caractere.')

lungime = 10
latime = 5
print(lungime * latime)
sqm = str(lungime * latime)
print('Aria dreptunghiului este: ' + sqm + '.')

enunt = 'Coral is either the stupidest animal or the smartest rock'
print(enunt.count('the'))
print(enunt.count('THE'))

assert enunt.isalnum() == True
print('Stringul nu contine doar numere.')







