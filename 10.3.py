class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.kerros = alinkerros
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros

    def ylös(self):
        if self.kerros < self.ylinkerros:
            self.kerros += 1
        return self.kerros

    def alas(self):
        if self.kerros > self.alinkerros:
            self.kerros -= 1
        return self.kerros

    def siirry(self, kohde):
        while self.kerros < kohde:
            self.ylös()
        while self.kerros > kohde:
            self.alas()
        return self.kerros

class Talo:
    def __init__(self, alinkerros, ylinkerros, hissilkm):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.hissit =  [Hissi(ylinkerros,alinkerros)for i in range(hissilkm)]

    def aja(self, hissinumero, kohdekerros):
        if 0 <= hissinumero <= len(self.hissit):
            hissi = self.hissit[hissinumero]
            hissi.siirry(kohdekerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry(self.alinkerros)
talo = Talo(1,10,2)

talo.aja(0,5)
talo.aja(1,7)

hissilkm = len(talo.hissit)
for hissinumero in range(hissilkm):
    hissi = talo.hissit[hissinumero]
    print(f"Hissi {hissinumero + 1} on kerroksessa {hissi.kerros}")

talo.palohälytys()

for hissinumero in range(hissilkm):
    hissi = talo.hissit[hissinumero]
    print(f"Hissi {hissinumero + 1} palautui kerrokseen {hissi.kerros}")