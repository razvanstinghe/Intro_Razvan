class ContBancar:
    # constructorul
    def __init__(self, titularCont, iban):

        # atribute, fielduri
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.activ = True
        self.pin = 7777
        self.incercari_activare = 0

    def interogareSold(self):
        print(f'Titular {self.titularCont}')
        print(f'Titular {self.iban}')
        print(f'Titular {self.sold}')
        print(f'Titular {self.activ}')
        print(f'Titular {self.incercari_activare}')
        print('------------------')

    def activareCont(self, pin_utilizator):
        self.salut()
        if pin_utilizator == self.pin:
            print('Card activat')
            self.activ = False
        else:
            print('PIN gresit')
            self.incercari_activare = self.incercari_activare + 1
            #self.incercari_activare+=1

    def alimentareCont(self, suma):
        self.salut()
        self.sold += suma
        print(f'Ati alimentat {suma}')
        print(f'Aveti in cont {self.sold}')

    def plataCard(self, suma):
        #variable scope
        self.salut()
        if suma <= self.sold:
            self.sold -= suma
            print(f'Ati cheltuit {suma}')
            print(f'Aveti in cont {self.sold}')
        else:
            print('Fonduri insuficiente')


    def salut(self):
        print(f'Buna {self.titularCont}')


