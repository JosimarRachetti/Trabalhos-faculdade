from uuid import uuid4
from model import visita, visitante, organização


def menu(opcao):
    print("1 - Cadastrar Visitante\n")
    print("2 - Cadastrar Organização\n")
    print("3 - Armazenar Visita\n")

    if opcao == "1":
        #Visitante
        cod_visitante = input("Digite o codigo do visitante: ")
        nome = input("Digite o nome do visitante: ")
        idade = input("Digite a idade do visitante: ")
        documento = input("Digite documento: ")
        registrar_visitante = visitante.Visitante(cod_visitante, nome, idade, documento)
        registrar_visitante.registro_visitante()
    elif opcao == "2":
        #Organização
        cod_contrato = input("Digite o codigo da organizacao: ")
        nome = input("Digite o nome da Organização: ")
        cnpj = input("Digite o cnpj da Organização: ")
        andar = input("Digite o andar da Organização: ")
        telefone = input("Digite o telefone da Organização: ")
        registrar_organizacao = organização.Organizacao(cod_contrato, nome, cnpj, andar, telefone)
        registrar_organizacao.registrar_organizacao()
    elif opcao == "3":
        #Visita
        cod_visita = input("Digite o codigo de visita: ")
        Horario = input("Digite o horario da visita: ")
        cod_visitante = input("Digite o codigo do visitante: ")
        cod_organizacao = input("Digite o codigo da Organizacao")
        registrar_visita = visita.Visita(cod_visita, Horario, cod_organizacao, cod_visitante)
        registrar_visita.registro_visita()
    else:
        print("opção inválida")