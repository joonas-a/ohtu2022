class Sovelluslogiikka:
    def __init__(self, tulos=0, edellinen=None):
        self.tulos = tulos
        self.edellinen = edellinen

    def miinus(self, arvo):
        self.aseta_arvo(self.tulos - arvo)

    def plus(self, arvo):
        self.aseta_arvo(self.tulos + arvo)

    def nollaa(self):
        self.aseta_arvo()

    def kumoa(self):
        if self.edellinen:
            self.tulos = self.edellinen
            self.edellinen = None

    def aseta_arvo(self, arvo=0):
        self.edellinen = self.tulos
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
        self.logiikka.kumoa()
