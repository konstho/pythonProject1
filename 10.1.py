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

hissi = Hissi(1,10)
hissi.siirry(5)

print("hissi on kerroksessa",hissi.kerros)
hissi.siirry(hissi.alinkerros)
print("hissi on kerroksessa", hissi.kerros)