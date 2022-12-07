import math

# class Car:
#     # fields(atribute)
#     make = 'Dacia'
#     model = None
#     year = 2022
#     color = None
#
#     # constructor. Se defineste ca la functii, doar ca trebuie sa aiba "__init__"
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color
#
# car1 = Car('Duster', 'white')
# car2 = Car('Logan', 'albastru')
#
# print(car1.make, car1.model, car1.color)
# # print(car1.model)
# # print(car1.color)


# class Angajat():
#     nume = input('Introduceti numele angajatului: ')
#     prenume = input('Introduceti prenumele angajatului: ')
#     salariu_lunar = int(input('Introduceti salariul angajatului: '))
#     salariu_anual = salariu_lunar * 12
#     crestere_salariu_procente = int(input('Introduceti cresterea salariala(%): '))
#     crestere_salariu_valoare = (salariu_lunar * crestere_salariu_procente) / 100
#     salariu_crescut = salariu_lunar + ((salariu_lunar * crestere_salariu_valoare) / 100)
#
#     def __init__(self, a, b, c, d, e, f, g):
#         self.nume = a
#         self.prenume = b
#         self.salariu_lunar = c
#         self.salariu_anual = d
#         self.crestere_salariu_procente = e
#         self.crestere_salariu_valoare = f
#         self.salariu_crescut = g
#
#     def descriere_angajat(self):
#         print(f'Date personale angajat Companie "X": ')
#
#     def nume_complet(self):
#         print(f'Numele si prenumele angajatului: {self.nume}, {self.prenume} .')
#
#     def salariul_lunar(self):
#         print(f'Salariul angajatului {self.nume}, {self.prenume} este: {self.salariu_lunar} EURO lunar.')
#         return self.salariu_lunar
#
#     def salariul_anual(self):
#         salariul_anual = self.salariu_anual
#         print(f'Salariul anual este: {self.salariu_anual} EURO.')
#         return self.salariu_anual
#
#     def marire_salariu_valoare(self):
#         salariu_marit = self.crestere_salariu_valoare
#         print(f'Salariul se mareste cu: {self.crestere_salariu_procente} %, reprezentand: {self.crestere_salariu_valoare} EURO.')
#         return self.crestere_salariu_valoare
#
#     def salariul_marit(self):
#         print(f'Noul salariu este de: {self.salariu_crescut} lunar.')
#         return self.salariu_crescut
#
# angajat = Angajat
# angajat.descriere_angajat(Angajat)
# angajat.nume_complet(Angajat)
# angajat.salariul_lunar(Angajat)
# angajat.salariul_anual(Angajat)
# angajat.marire_salariu_valoare(Angajat)
# angajat.salariul_marit(Angajat)

# class Cont():
#
#     iban = 'RO0000INGB000000000'
#     titular_cont = input('Introduceti numele si prenumele titularului de cont: ')
#     sold = int(input('Sold disponibil: '))
#     se_debiteaza = int(input('Introduceti suma pe care doriti sa o retrageti din cont: '))
#     se_crediteaza = int(input('Introduceti suma pe care doriti sa o adaugati in cont: '))
#     sold_final_cont = sold - se_debiteaza + se_crediteaza
#
#     def __init__(self, a, b, c, d, e, f):
#         self.iban = a
#         self.titular_cont = b
#         self.sold = c
#         self.se_debiteaza = d
#         self.se_crediteaza = e
#         self.sold_final_cont = f
#
#     def afisare_iban(self):
#         print(f'Cont IBAN: {self.iban}')
#
#     def afisare_titula_cont(self):
#         print(f'Numele titulatului de cont este: {self.titular_cont}')
#
#     def afisare_sold(self):
#         print(f'Soldul titularului de cont {self.titular_cont} este de: {self.sold} RON.')
#         return self.sold
#     def debitare_cont_suma(self):
#         print(f'Suma debitata este:  {self.se_debiteaza} RON.')
#         return self.se_debiteaza
#     def creditare_cont_suma(self):
#         print(f'Contul s-a incarcat cu suma {self.se_crediteaza} RON.')
#         return self.se_crediteaza
#     def sold_total(self):
#         print(f'Soldul total este: {self.sold_final_cont} RON.')
#         return self.sold_final_cont
#
#
# cont_bancar = Cont
# cont_bancar.afisare_iban(Cont)
# cont_bancar.afisare_titula_cont(Cont)
# cont_bancar.afisare_sold(Cont)
# cont_bancar.debitare_cont_suma(Cont)
# cont_bancar.creditare_cont_suma(Cont)
# cont_bancar.sold_total(Cont)


# class Cont():
#
#     iban = 'RO0000INGB000000000'
#     titular_cont = input('Introduceti numele si prenumele titularului de cont: ')
#     sold = int(input('Sold disponibil: '))
#     # se_debiteaza = int(input('Introduceti suma pe care doriti sa o retrageti din cont: '))
#     # se_crediteaza = int(input('Introduceti suma pe care doriti sa o adaugati in cont: '))
#     # sold_final_cont = sold - se_debiteaza + se_crediteaza
#
#     def __init__(self, a, b, c):
#         self.iban = a
#         self.titular_cont = b
#         self.sold = c
#         # self.se_debiteaza = d
#         # self.se_crediteaza = e
#         # self.sold_final_cont = f
#
#     def afisare_iban(self):
#         print(f'Cont IBAN: {self.iban}')
#
#     def afisare_titula_cont(self):
#         print(f'Numele titulatului de cont este: {self.titular_cont}')
#
#     def afisare_sold(self):
#         print(f'Soldul titularului de cont {self.titular_cont} este de: {self.sold} RON.')
#         # return self.sold
#         se_debiteaza = int(input('Introduceti suma pe care doriti sa o retrageti din cont: '))
#         print(f'Suma debitata este:  {self.se_debiteaza} RON.')
#         # return self.se_debiteaza
#         print(f'Contul s-a incarcat cu suma {self.se_crediteaza} RON.')
#         se_crediteaza = int(input('Introduceti suma pe care doriti sa o adaugati in cont: '))
#         # return self.se_crediteaza
#         print(f'Soldul total este: {self.sold_final_cont} RON.')
#         sold_final_cont = int(sold) - se_debiteaza + se_crediteaza
#         return self.sold_final_cont
    # def debitare_cont_suma(self):
    #     print(f'Suma debitata este:  {self.se_debiteaza} RON.')
    #     return self.se_debiteaza
    # def creditare_cont_suma(self):
    #     print(f'Contul s-a incarcat cu suma {self.se_crediteaza} RON.')
    #     return self.se_crediteaza
    # def sold_total(self):
    #     print(f'Soldul total este: {self.sold_final_cont} RON.')
    #     return self.sold_final_cont


# cont_bancar = Cont
# cont_bancar.afisare_iban(Cont)
# cont_bancar.afisare_titula_cont(Cont)
# cont_bancar.afisare_sold(Cont)
# cont_bancar.debitare_cont_suma(Cont)
# cont_bancar.creditare_cont_suma(Cont)
# cont_bancar.sold_total(Cont)

print('--------------exercitiul 1--------------')

class Cerc:

    raza = int(input('Introdu valoarea razei cercului: '))
    culoare = input('Introdu culoarea cercului: ')
    # arie = math.pi * raza * raza
    # diametru = raza * 2
    # circumferinta = 2 * math.pi * raza

    def __init__(self, a, b):
        self.raza = a
        self.culoare = b
        # self.arie = c
        # self.diametru = d
        # self.circumferinta = e


    def descriere_cerc(self):
        print(f'Raza cercului este: {self.raza}')
        print(f'Culoarea cercului este: {self.culoare}')

    def arie_cerc(self):
        arie_cerc = math.pi * self.raza * self.raza
        print(f'{self.arie_cerc}')
        return {self.arie_cerc}

    def diametru_cerc(self):
        diametru_cerc = 2 * self.raza
        print(f'Diametrul cercului este: {self.diametru_cerc}')
        return {self.diametru_cerc}

    def circumferinta_cerc(self):
        circumferinta_cerc = 2 * math.pi * self.raza
        print(f'Circumferinta cercului este: {self.circumferinta_cerc}')
        return {self.circumferinta_cerc}

rezultat = Cerc
rezultat.descriere_cerc(Cerc)
rezultat.arie_cerc(Cerc)
rezultat.diametru_cerc(Cerc)
rezultat.circumferinta_cerc(Cerc)