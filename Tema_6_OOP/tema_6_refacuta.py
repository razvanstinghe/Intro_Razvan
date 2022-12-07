class Cerc:   # FUNCTIILE se numesc METODE

    print('--------------exercitiul 1--------------')
    import math

    raza = int(input('Introdu valoarea razei cercului: '))
    culoare = 'Verde'
    arie = math.pi * raza * raza
    diametru = raza * 2
    circumferinta = 2 * math.pi * raza

    def __init__(self, a, b, c, d, e):
        self.raza = a
        self.culoare = b
        self.arie = c
        self.diametru = d
        self.circumferinta = e


    def printeaza_descriere_cerc(self):

        print(f'Raza cercului este: {self.raza}')
        print(f'Culoarea cercului este: {self.culoare}')

    def returneaza_arie_cerc(self):
        print(f'{self.arie}')
        return {self.arie}

    def returneaza_diametru(self):
        print(f'Diametrul cercului este: {self.diametru}')
        return {self.diametru}

    def returneaza_circumferinta(self):
        print(f'Circumferinta cercului este: {self.circumferinta}')
        return {self.circumferinta}

rezultat = Cerc
rezultat.printeaza_descriere_cerc(Cerc)
rezultat.returneaza_arie_cerc(Cerc)
rezultat.returneaza_diametru(Cerc)
rezultat.returneaza_circumferinta(Cerc)

print('--------------exercitiul 2--------------')
class Dreptunghi:


    lungime = int(input('Introdu valoarea lungimii: '))
    latime = int(input('Introdu valoarea latimii: '))
    arie_dreptunghi = lungime * latime
    perimetru_dreptunghi = (2*lungime) + (2*latime)
    culoare = input('Introdu culoarea: ')
    noua_culoare = input('Introdu noua culoare a dreptunghiului: ')

    def __init__(self, a, b, c, d, e, f):
        self.lungime = a
        self.latime = b
        self.arie_dreptunghi = c
        self.perimetru_dreptunghi = d
        self.culoare = e
        self.noua_culoare = f

    def descriere_dreptunghi(self):
        print(f'Lungimea dreptunghiului este: {self.lungime}')
        print(f'Latimea dreptunghiului este: {self.latime}')
        print(f'Culoarea initiala a dreptunghiului este: {self.culoare}')

    def aria_dreptunghi(self):
        print(f'Aria dreptunghiului este: {self.arie_dreptunghi}')
        return {self.arie_dreptunghi}

    def perimetrul_dreptunghi(self):
        print(f'Perimetrul dreptunghiului este: {self.perimetru_dreptunghi}')
        return {self.perimetru_dreptunghi}

    def schimba_culoare(self):
        self.culoare == self.noua_culoare
        # print(f'Lungimea dreptunghiului este: {self.lungime}')
        # print(f'Latimea dreptunghiului este: {self.latime}')
        print(f'Culoarea noua a dreptunghiului este: {self.noua_culoare}')





rezultat = Dreptunghi
rezultat.descriere_dreptunghi(Dreptunghi)
rezultat.aria_dreptunghi(Dreptunghi)
rezultat.perimetrul_dreptunghi(Dreptunghi)
rezultat.schimba_culoare(Dreptunghi)


print('--------------exercitiul 3--------------')

class Angajat():
    nume = input('Introduceti numele angajatului: ')
    prenume = input('Introduceti prenumele angajatului: ')
    salariu_lunar = int(input('Introduceti salariul angajatului: '))
    salariu_anual = salariu_lunar * 12
    crestere_salariu_procente = int(input('Introduceti cresterea salariala(%): '))
    crestere_salariu_valoare = (salariu_lunar * crestere_salariu_procente) / 100
    salariu_crescut = salariu_lunar + crestere_salariu_valoare

    def __init__(self, a, b, c, d, e, f, g):
        self.nume = a
        self.prenume = b
        self.salariu_lunar = c
        self.salariu_anual = d
        self.crestere_salariu_procente = e
        self.crestere_salariu_valoare = f
        self.salariu_crescut = g

    def descriere_angajat(self):
        print(f'Date personale angajat Companie "X": ')

    def nume_complet(self):
        print(f'Numele si prenumele angajatului: {self.nume}, {self.prenume} .')

    def salariul_lunar(self):
        print(f'Salariul angajatului {self.nume}, {self.prenume} este: {self.salariu_lunar} EURO lunar.')
        return self.salariu_lunar

    def salariul_anual(self):
        salariul_anual = self.salariu_anual
        print(f'Salariul anual este: {self.salariu_anual} EURO.')
        return self.salariu_anual

    def marire_salariu_valoare(self):
        salariu_marit = self.crestere_salariu_valoare
        print(f'Salariul se mareste cu: {self.crestere_salariu_procente} %, reprezentand: {self.crestere_salariu_valoare} EURO.')
        return self.crestere_salariu_valoare

    def salariul_marit(self):
        print(f'Noul salariu este de: {self.salariu_crescut} lunar.')
        return self.salariu_crescut

angajat = Angajat
angajat.descriere_angajat(Angajat)
angajat.nume_complet(Angajat)
angajat.salariul_lunar(Angajat)
angajat.salariul_anual(Angajat)
angajat.marire_salariu_valoare(Angajat)
angajat.salariul_marit(Angajat)

print('--------------exercitiul 4--------------')

class Cont():

    iban = 'RO0000INGB000000000'
    titular_cont = input('Introduceti numele si prenumele titularului de cont: ')
    sold = int(input('Sold disponibil: '))
    se_debiteaza = int(input('Introduceti suma pe care doriti sa o retrageti din cont: '))
    se_crediteaza = int(input('Introduceti suma pe care doriti sa o adaugati in cont: '))
    sold_final_cont = sold - se_debiteaza + se_crediteaza

    def __init__(self, a, b, c, d, e, f):
        self.iban = a
        self.titular_cont = b
        self.sold = c
        self.se_debiteaza = d
        self.se_crediteaza = e
        self.sold_final_cont = f

    def afisare_iban(self):
        print(f'Cont IBAN: {self.iban}')

    def afisare_titula_cont(self):
        print(f'Numele titulatului de cont este: {self.titular_cont}')

    def afisare_sold(self):
        print(f'Soldul titularului de cont este de: {self.sold} RON.')
        return self.sold
    def debitare_cont_suma(self):
        print(f'Suma debitata este:  {self.se_debiteaza} RON.')
        return self.se_debiteaza
    def creditare_cont_suma(self):
        print(f'Contul s-a incarcat cu suma {self.se_crediteaza} RON.')
        return self.se_crediteaza
    def sold_total(self):
        print(f'Soldul total este: {self.sold_final_cont} RON.')
        return self.sold_final_cont


cont_bancar = Cont
cont_bancar.afisare_iban(Cont)
cont_bancar.afisare_titula_cont(Cont)
cont_bancar.afisare_sold(Cont)
cont_bancar.debitare_cont_suma(Cont)
cont_bancar.creditare_cont_suma(Cont)
cont_bancar.sold_total(Cont)



