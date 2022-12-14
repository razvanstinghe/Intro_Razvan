# ABSTRACTION
# Clasa abstractă FormaGeometrica
# Conține un field PI=3.14
# Conține o metodă abstractă aria (opțional)
# Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
# probabil am colturi’

# INHERITANCE
# Clasa Pătrat - moștenește FormaGeometrica
# constructor pentru latură
# ENCAPSULATION
# latura este proprietate privată
# Implementează getter, setter, deleter pentru latură
# Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
# implementezi metoda abstractă aria)
# Clasa Cerc - moștenește FormaGeometrica
# constructor pentru rază
# raza este proprietate privată
# Implementează getter, setter, deleter pentru rază
# Implementează metoda cerută de interfață - în calcul folosește field PI
# mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
# abstractă aria)

# POLYMORPHISM
# Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
# Creează un obiect de tip Patrat și joacă-te cu metodele lui
# Creează un obiect de tip Cerc și joacă-te cu metodele lui.
import math

from abc import abstractmethod, ABC


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descriere(self):
        print('Cel mai probabil am colturi.')


FormaGeometrica.descriere(FormaGeometrica)


class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    def aria(self):
        self.aria = self.latura * self.latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: Latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Setter: Latura este {latura}')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print(f'Deleter: Am sters latura')
        self.__latura = None


patrat2 = Patrat(4)
patrat2.latura = 3
patrat2.latura
del patrat2.latura
patrat2.latura


class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        self.aria = self.PI*(self.raza * self.raza)

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: Raza este {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Setter: Raza este {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print(f'Deleter: Am sters raza')
        self.__raza = None


cerc2 = Cerc(4)
cerc2.raza = 3
cerc2.raza
cerc2.raza
del cerc2.raza
cerc2.raza



def descrie_polii():
    print("Eu nu am colturi")

descrie_polii()

class Dreptunghi():
    def lungime(self):
        print("Introduce lungimea dreptunghiului.")

    def nr_laturi(self):
        print('Dreptunghiul are 4 laturi')
    def nr_unghiuri(self):
        print('Dreptunghiul are 4 unghiuri')

class Triunghi():
    def lungime(self):
        print("Ipotenuza este latura mai lunga.")
    def nr_laturi(self):
        print('Triunghiul are 3 laturi.')
    def nr_unghiuri(self):
        print('Triunghiul are 3 ughiuri.')

obj_laturi = Dreptunghi()
obj_laturi.lungime()
obj_laturi.nr_laturi()
obj_laturi.nr_unghiuri()

obj_triunghi = Triunghi()
obj_triunghi.lungime()
obj_triunghi.nr_laturi()
obj_triunghi.nr_unghiuri()
# for dimensiune in (obj_laturi, obj_paral):
#     dimensiune.lungime()



