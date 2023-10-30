class auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

uus_auto = auto("abc-123",142)

print(f"auton rekisteritunnus:{uus_auto.rekisteri}")
print(f"auton huippunopeus: {uus_auto.huippunopeus}")
print(f"auton nopeus: {uus_auto.nopeus}")
print(f"auton matka: {uus_auto.matka}")