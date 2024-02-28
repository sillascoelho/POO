class Vigas:

    vigasCriadas = []

    def __init__(self, nome, base, altura, comprimentoTotal, fck, cobrimento):

        self.nome = nome
        self.base = base
        self.altura = altura
        self.comprimentoTotal = comprimentoTotal
        self.fck = fck
        self.cobrimento = cobrimento
        Vigas.vigasCriadas.append(self)

    def __str__(self):
        return f'{self.nome} - {self.base} X {self.altura}'

    def volumeConcreto(self):

        volumeConc = (self.base / 100) * (self.altura / 100) * (self.comprimentoTotal / 100)

        return f'O volume da viga é de {round(volumeConc, 2)} m³'

    def formaViga(self):

        perimetro = (2 * self.base) + (2 * self.altura)

        forma = perimetro * self.comprimentoTotal

        return f'A quantidade de fôrmas da viga é {round(forma / 10**4, 2)} m²'
    
    def listarVigas():

        for viga in Vigas.vigasCriadas:

            print(viga)

viga_01 = Vigas('Viga 01', 25, 45, 600, 25, 2.5)
viga_02 = Vigas('Viga 02', 30, 60, 800, 30, 3)
viga_03 = Vigas('Viga 03', 40, 100, 1000, 32, 3)

Vigas.listarVigas()