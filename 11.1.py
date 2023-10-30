class tekijä:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta(self):
        print("tekijän nimi on: ", self.nimi)

class Kirja(tekijä):
    def __init__(self, nimi, kirja, sivumäärä):
        super().__init__(nimi)
        self.kirja = kirja
        self.sivumäärä = sivumäärä

    def tulosta(self):
        super().tulosta()
        print("kirjan nimi: ", self.kirja)
        print("kirjan sivumäärä: ",self.sivumäärä)

class Lehti(tekijä):
    def __init__(self, nimi, lehti):
        super().__init__(nimi)
        self.lehti = lehti

    def tulosta(self):
        super().tulosta()
        print("lehden nimi on: ",self.lehti)


kirja = Kirja("rosa liksom", "hytti no6", 200)
lehti = Lehti("aki hyyppä","aku ankka")

kirja.tulosta()
print()
lehti.tulosta()