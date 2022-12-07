class CarPy:
    car2 = CarPy('gray')
    car2.color = 'red'
    car2.color
    del car2.color
    car2.color

    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.getter
    def color(self):
        print(f'Getter: Culoarea este {self.__color}')
        return self.__color

    @color.setter
    def color(self):
        print(f'Setter: Noua culoare este {color}')

    @color.deleter
    def color(self):
        print(f'Am sters culoarea.')
        self.__color = None



