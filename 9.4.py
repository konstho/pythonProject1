import random
class Auto:
    def __init__(self,rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        uus_nopeus = self.nopeus+muutos
        if uus_nopeus < 0:
            uus_nopeus = 0
        if uus_nopeus > self.huippunopeus:
            uus_nopeus = self.huippunopeus
        self.nopeus = uus_nopeus

    def matka1(self,kulje):
        uusmatka = self.nopeus*kulje
        self.matka = uusmatka

autot = []
for i in range(10):
    rekisteri = "abc-"+str(i+1)
    huippunopeus = random.randint(100,200)
    auto = Auto(rekisteri, huippunopeus)
    autot.append(auto)

kilpailu_jatkuu = True

while True:
    for auto in autot:
        muutos = random.randint(-10,15)
        auto.kiihdytä(muutos)
        auto.matka1(1)

    for auto in autot:
        if auto.matka >= 10000:
            kilpailu_jatkuu = False
            break

print("{:<10} {:<15} {:<15} {:<20}".format("Rekisteri", "Huippunopeus (km/h)", "Nykyinen nopeus (km/h)", "Kuljettu matka (km)"))
print("-" * 60)
for auto in kilpa_autot:
    print("{:<10} {:<15} {:<15} {:<20}".format(auto.rekisteritunnus, auto.huippunopeus, auto.nykyinen_nopeus, auto.kuljettu_matka))