from pesquisa import Pesquisa

class PesquisaSaude(Pesquisa):
    def __init__(self, perguntas):
        super().__init__(perguntas)

    def validar_resposta(self, resposta):
        return resposta in [1, 2, 3]
