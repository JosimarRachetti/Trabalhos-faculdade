from controller import menu_alugueis, menu_contratos, menu_predio, menu_recepcao, menu_servicos


def menu():
    print("MENU\n\n")
    print("Selecione a opção: \n")
    print("1 - cadastro de locatario, locador, imoveis \n")
    print("2 - cadastro de contratos e contas \n")
    print("3 - recepção de visitantes \n")
    print("4 - predio e uso estacionamento \n")
    print("5 - serviços e contas\n")
    print("6 - materiais\n")

    opcao = input("Digite a opcao: ")

    if opcao == "1":
        _menu_aluguel()
    elif opcao == "2":
        _menu_contrato()
    elif opcao == "3":
        _menu_recepcao()
    elif opcao == "4":
        _menu_predio()
    elif opcao == "5":
        _menu_servicos()
    elif opcao == "6":
        _menu_materiais()
    else:
        print("opção não valida\n")


def _menu_aluguel():
    print("1 - Cadastrar Locatario\n")
    print("2 - Cadastrar Locador\n")
    print("3 - Cadastrar Imovel\n")
    print("0 - voltar Menu anterior\n")

    opcao = input("digite a opcao: ")

    if opcao == "0":
        menu()

    menu_alugueis.menu(opcao)


def _menu_contrato():
    print("1 - Cadastrar Contrato Imovel\n")
    print("2 - Cadastrar Contrato Servico\n")
    print("3 - Cadastrar Contas\n")
    print("4 - Armazenar Contrato\n")
    print("5 - Cadastrar cotas condominio")
    print("0 - voltar Menu anterior\n")

    opcao = input("digite a opcao: ")

    if opcao == "0":
        menu()

    menu_contratos.menu(opcao)


def _menu_recepcao():
    print("1 - Cadastrar Visitante\n")
    print("2 - Cadastrar Organização\n")
    print("3 - Cadastrar Visita\n")
    print("0 - voltar Menu anterior\n")

    opcao = input("digite a opcao: ")

    if opcao == "0":
        menu()

    menu_recepcao.menu(opcao)


def _menu_predio():
    print("1 - Cadastrar Predio\n")
    print("2 - Cadastrar uso de vagas\n")
    print("0 - voltar Menu anterior\n")

    opcao = input("digite a opcao: ")

    if opcao == "0":
        menu()

    menu_predio.menu(opcao)


def _menu_servicos():
    print("1 - Registrar servico manuntencao elevador\n")
    print("2 - Registrar servico limpeza\n")
    print("3 - Registrar funcionarios\n")
    print("0 - voltar Menu anterior\n")

    opcao = input("digite a opcao: ")
    if opcao == "0":
        menu()

    menu_servicos.menu(opcao)


def _menu_materiais():
    print("1 - Registrar materiais\n")
    print("2 - Registrar pedido materiais\n")
    print("0 - voltar Menu anterior\n")
