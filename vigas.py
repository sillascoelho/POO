class Vigas:

    def __init__(self, base, altura, comprimentoTotal, fck, cobrimento):
        self.base = base
        self.altura = altura
        self.comprimentoTotal = comprimentoTotal
        self.fck = fck
        self.cobrimento = cobrimento

    def volumeConcreto(self):

        volumeConc = (self.base / 100) * (self.altura / 100) * (self.comprimentoTotal / 100)

        return f'O volume da viga é de {round(volumeConc, 2)} m³'

    def formaViga(self):

        perimetro = (2 * self.base) + (2 * self.altura)

        forma = perimetro * self.comprimentoTotal

        return f'A quantidade de fôrmas da viga é {round(forma / 10**4, 2)} m²'

viga_01 = Vigas(20, 100, 900, 35, 3) 

viga_02 = Vigas(15, 50, 600, 30, 3)

print(viga_02.formaViga())

print(viga_02.volumeConcreto())