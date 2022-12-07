class Figura_geometrica:

    import math

    # lungime_latura = None  # None inseamna ca nu sunt definite. Aici definim atributele.
    # latime_latura = None
    # raza = None

    def __init__(self, a, b, c):       # se creeza un constructor.
        self.lungime_latura = a
        self.latime_latura = b
        self.raza = c

    def printeaza_lungimea(self):   # reprezinta metoda, adica functia (terminoligia veche).
        # Aici se definesc metodele prin "def"
        print(f'Lungimea este:  {self.lungime_latura}')

