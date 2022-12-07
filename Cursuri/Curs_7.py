# try:                     # am tratat exeptiile
#     assert  1 == 2, 'comparatia nu este corecta'  # propozitia dintre ghilimele este atribuita AssertionError
# except AssertionError as e:   # e = error
#     print(e, ' programul nu a executat linia respectiva')
#
# print('Hello')
print('---------exercitiul urmator- MOSTENIREA------------------')

# class Masina:
#     def numar_roti(self):
#         print('Masina are 4 roti.')
#
# class Jeep(Masina):
#     def suspensii(self):
#         print('Jeepul are suspensii mari.')
#
# hummer = Jeep()
# hummer.numar_roti()
# hummer.suspensii()
# logan = Jeep()
# logan.numar_roti()
# logan.suspensii()
# ford = Masina()
# ford.numar_roti()


print('---------exercitiul urmator-------------------')  # mai sus avem MOSTENIREA (INHERITANCE)


from abc import  abstractmethod, ABC

class Masina(ABC):   # aici implementam o clasa abstracta (o clasa) # prin scrierea "ABC" se ->>>
                        # ->>> transforma clasa intr-una abstracta. ABC=abstract
    @abstractmethod
    def numar_roti(self):
        raise NotImplementedError

    @abstractmethod
    def culoare(self):
        raise NotImplementedError


class SUV(Masina):
    def __suspensii(self):
        print('Jeepul are suspensii mari.')

    def numar_roti(self):
        print('4 roti de teren')

    def culoare(self):
        print('neagra')


class Sport(Masina):
    def numar_roti(self):
        print('4 roti de circuit')

    def culoare(self):
        print('albastra')


ferrari = Sport()
ferrari.numar_roti()
volvo = SUV()
volvo.culoare()  # aici am implementat polimorfismul
ferrari.culoare() # aici am implementat polimorfismul
# volvo.suspensii()
try:
    volvo.suspensii()
except:   # e = error
    print('sunt expert pe tratarea erorilor')