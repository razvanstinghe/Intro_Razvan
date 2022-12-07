class Automobil:
    # la inceput definim atributele
    numar_roti = 2
    forma = None
    culoare = None
    numar_usi = 2

    # mai jos definim metode:

    def printeaza_numar_roti(self):          # aici se definesc metodele prin "def"
        if self.numar_roti == 2:
            print(f'Nr de roti este: {self.numar_roti}')
            print(f'Automobilul nostru este motocicleta.')

    def printeaza_forma(self, tablarie):
        self.forma = tablarie
        if self.forma == "SUV":
            print(f'Forma este: {self.forma}')
            print(f'SUV')
        elif self.numar_usi == 0:
            print(f'Nr de usi este: {self.numar_usi}')
            print(f'Automobilul nostru este masina motocicleta.')
        elif self.numar_usi == 4:
            print(f'Nr de usi este: {self.numar_usi}')
            print(f'Automobilul nostru este masina de familie.')

    def printeaza_culoare(self):
        if self.numar_roti == 2:
            print(f'Nr de roti este: {self.numar_roti}')
            print(f'Automobilul nostru este motocicleta.')

    def printeaza_numar_usi(self):
        if self.numar_usi == 2:
            print(f'Nr de usi este: {self.numar_usi}')
            print(f'Automobilul nostru este masina sport.')
        elif self.numar_usi == 0:
            print(f'Nr de usi este: {self.numar_usi}')
            print(f'Automobilul nostru este masina motocicleta.')
        elif self.numar_usi == 4:
            print(f'Nr de usi este: {self.numar_usi}')
            print(f'Automobilul nostru este masina de familie.')
# mai jos am facut o initializare. Am initializat clasa "Automobil" in clasa "caruta"
caruta = Automobil()


# Acum folosim proprietatile obiectului "caruta".

# 1: Apelarea de atribute
# print(caruta.numar_usi)
#2: apelarea de metode
# caruta.printeaza_numar_usi()

# 3: apelarea de metode cu argumente
# caruta.printeaza_forma()
