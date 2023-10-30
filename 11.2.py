class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        uus_nopeus = self.nopeus + muutos
        if uus_nopeus < 0:
            uus_nopeus = 0
        if uus_nopeus > self.huippunopeus:
            uus_nopeus = self.huippunopeus
        self.nopeus = uus_nopeus

    def kulje(self, tunti):
        matka1 = self.nopeus *tunti
        self.matka += matka1

class Sähköauto(Auto):
    def __init__(self,rekisteri, huippunopeus, akku):
        super().__init__(rekisteri, huippunopeus)
        self.akku = akku

class Moottoriauto(Auto):
    def __init__(self, rekisteri, huippunopeus, tankki):
        super().__init__(rekisteri, huippunopeus)
        self.tankki = tankki

sähköauto = Sähköauto("abc-15",180,52.5)
moottoriauto = Moottoriauto("acd-123", 165, 32.3)

sähköauto.kiihdytä(60)
moottoriauto.kiihdytä(100)

for i in range(3):
    sähköauto.kulje(1)
    moottoriauto.kulje(1)

print("sähköauton matka: ",sähköauto.matka)
print("moottoriauton matka: ",moottoriauto.matka)