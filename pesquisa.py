import os
import csv
from datetime import datetime

class Pesquisa:
    def __init__(self, perguntas):
        self.perguntas = perguntas

    def realizar_pesquisa(self):
        if not os.path.exists('dados_pesquisa.csv') or os.path.getsize('dados_pesquisa.csv') == 0:
            with open('dados_pesquisa.csv', 'w', newline='') as arquivo_csv:
                escritor_csv = csv.writer(arquivo_csv)
                escritor_csv.writerow(['Idade', 'Genero', 'Atividade física', 'Consumo de frutas e vegetais',
                                       '7 horas de sono', 'Tabagismo','Bebidas','Meditação/Yoga','Check-ups Médicos', 'Data', 'Hora'])

        with open('dados_pesquisa.csv', 'a', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            while True:
                dados_participante = self.coletar_dados_participante()
                if dados_participante is None:
                    break
                escritor_csv.writerow(dados_participante)

        print("Dados salvos com sucesso no arquivo 'dados_pesquisa.csv'!")
    def coletar_dados_participante(self):
        idade = input("Informe a sua idade (00 para sair): ")
        if idade == '00':
            return None
        if not self.validar_idade(idade):
            print("Idade inválida. Por favor, informe a sua idade novamente.")
            return self.coletar_dados_participante()
        generos=["Masculino", "Feminino", "Não binário", "Agênero", "Gênero fluido", "Bigênero", "Transgênero", "Intersexo", "Outro"," Prefiro não dizer"]
        genero = int(input("Qual o seu gênero?\n1- Masculino\n2- Feminino\n3- Não binário\n4- Agênero\n5- Gênero "
                       "fluido\n6- Bigênero\n7- Transgênero\n8- Intersexo\n9- Outro\n10- Prefiro não dizer\n>> "))
        while not self.validar_genero(genero):
            genero = int(input("Opção inválida. Por favor, selecione uma das opções de gênero listadas: "))
            
        respostas = []
        for pergunta in self.perguntas:
            resposta = int(input(pergunta))
            while not self.validar_resposta(resposta):
                resposta = int(input("Resposta inválida. Por favor, selecione uma das opções listadas: "))
            respostaPerguntas=["Sim", "Não", "Não Sabe"] 
            validacaoPerguntas=self.validar_resposta(resposta)
            if validacaoPerguntas==1 or validacaoPerguntas==2 or validacaoPerguntas==3:
                respostas.append(respostaPerguntas[resposta-1]) 
        data_atual = datetime.now().strftime('%Y-%m-%d')
        hora_atual = datetime.now().strftime('%H:%M:%S')

        return [idade, generos[genero-1]] + respostas + [data_atual, hora_atual]

    def validar_idade(self, idade):
        try:
            idade = int(idade)
            return 0 <= idade <= 120
        except ValueError:
            return False

    def validar_genero(self, genero):
        return genero in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def validar_resposta(self, resposta):
        return resposta in [1, 2, 3]
