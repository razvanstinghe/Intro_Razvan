print('---------ABSTRACTION--------------')

# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
# probabil am colturi’
import math

from abc import abstractmethod, ABC


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

class Descriere(FormaGeometrica):
    def aria(self):
        print('Aria. ')

    def descriere(self):
        print('Cel mai probabil am colturi.')

descriere = Descriere()
descriere.aria()
descriere.descriere()


print('---------INHARITANCE--------------')


# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură

class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = 5

# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să implementezi metoda abstractă aria)
    @property
    def lungime(self):
        return self.__latura
    @lungime.getter
    def lungime(self):
        print(f'Getter: Lungimea laturii este {self.__latura}')

    @lungime.setter
    def lungime(self, latura):
        print(f'Setter: Noua lungime este {latura}')

    @lungime.deleter
    def lungime(self, latura):
        print(f'Deleter: Am sters lungimea laturii.')
        self.__latura = None

ariee = FormaGeometrica()
ariee.aria()

