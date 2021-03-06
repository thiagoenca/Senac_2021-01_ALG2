from Atividades.Atividade3.Classes.Automovel import Automovel
from ClassesAuxiliares.FormatFonts import FormatFonts

fonte = FormatFonts()


class Carro(Automovel):
    def __init__(self, marca, qtd_rodas, modelo, potencia_motor, qtd_portas):
        super().__init__(marca, qtd_rodas, modelo, potencia_motor)
        self.qtd_portas = int(qtd_portas)

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print(f'    {fonte.green("Quantidade de portas:")} {self.qtd_portas}')
