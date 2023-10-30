class auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka1 = 0

    def kiihdytä(self, muutos):
        uus_nopeus = self.nopeus + muutos
        if uus_nopeus < 0:
            uus_nopeus = 0
        if uus_nopeus > self.huippunopeus:
            uus_nopeus = self.huippunopeus
        self.nopeus = uus_nopeus

    def kulje(self, tunti):
        matka = self.nopeus *tunti
        self.matka1 += matka

uus_auto = auto("abc-123",142)

uus_auto.kiihdytä(100)
uus_auto.kiihdytä(20)
uus_auto.kiihdytä(50)

print("auton nykyinen nopeus:", uus_auto.nopeus, "km/h")
uus_auto.kiihdytä(-1)
print("hätäjarrutuksen jälkeen nopeus:", uus_auto.nopeus, "km/h")
uus_auto.kulje(2)
print("kuljettu matka:", uus_auto.matka1, "km")