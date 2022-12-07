from oop_curs_prezentare.cont_bancar import ContBancar

cont1 = ContBancar('Andi S', 'RO001')
cont2 = ContBancar('Crina S', 'RO002')

cont1.activareCont(7777)
cont2.activareCont(3333)
cont2.activareCont(7777)

cont1.alimentareCont(300)
cont2.alimentareCont(700)
cont2.alimentareCont(300)

cont1.plataCard(500)
cont1.plataCard(300) #0
cont2.plataCard(100)
cont2.plataCard(200) #700


cont1.interogareSold()
cont2.interogareSold()