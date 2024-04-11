from pesquisaSaude import PesquisaSaude

def main():
    perguntas_saude = [
    "Você pratica atividade física regularmente? \n 1 - Sim \n 2 - Não \n 3 - Não sei responder:\n>> ",
    "Você consome pelo menos 5 porções de frutas e vegetais por dia? \n 1 - Sim \n 2 - Não \n 3 - Não sei responder:\n>> ",
    "Você costuma dormir pelo menos 7 horas por noite? \n 1 - Sim \n 2 - Não \n 3 - Não sei responder:\n>> ",
    "Você fuma atualmente? \n 1 - Sim \n 2 - Não \n 3 - Não sei responder:\n>> ",
    "Você consome bebidas alcoólicas regularmente? \n 1 - Sim \n 2 - Não \n 3 - Não sei responder:\n>> ",
    "Você costuma realizar check-ups médicos regularmente? \n 1 - Sim \n 2 - Não \n 3 - Não sei responder:\n>> "
]

    pesquisa_saude = PesquisaSaude(perguntas_saude)

    print("### Pesquisa sobre Saúde ###")
    pesquisa_saude.realizar_pesquisa()

if __name__ == "__main__":
    main()
