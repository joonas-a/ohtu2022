class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def kumoa(self):
        pass

    def aseta_arvo(self, arvo):
        self.tulos = arvo

class Summa():
    def __init__(self, logiikka, syote):
        self.logiikka = logiikka
        self.syote = syote

    def suorita(self):
        return self.logiikka.plus(self.syote())

class Erotus():
    def __init__(self, logiikka, syote):
        self.logiikka = logiikka
        self.syote = syote

    def suorita(self):
        return self.logiikka.miinus(self.syote())

class Nollaus():
    def __init__(self, logiikka, syote):
        self.logiikka = logiikka
        self.syote = syote

    def suorita(self):
        self.logiikka.nollaa()

class Kumoa():
    def __init__(self, logiikka, syote):
        self.logiikka = logiikka
        self.syote = syote

    def suorita(self):
        pass
