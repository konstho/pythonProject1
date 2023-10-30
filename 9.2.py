class auto:
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

auto1 = auto("abc-123",142)

auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)

print("auton nykyinen nopeus:", auto1.nopeus, "km/h")
auto1.kiihdytä(-200)
print("hätäjarrutuksen jälkeen nopeus:", auto1.nopeus, "km/h")