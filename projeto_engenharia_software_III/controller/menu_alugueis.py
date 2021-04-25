from model import locatario, locador, imovel
import const
from uuid import uuid4


def menu(opcao):
    if opcao == "1":
        # Locatario
        cnpj = input("Digite o cnpj: ")
        razao_social = input("Digite a razao social: ")
        responsavel = input("Digite o responsavel: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        _Locatario = locatario.Locatario(cnpj, razao_social, responsavel, telefone, email)
        _Locatario.cadastrar_locatario()
    elif opcao == "2":
        # Locador
        registro_nacional = input("Digite o registro nacional: ")
        nome = input("Digite o nome: ")
        responsavel = input("Digite o responsavel: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        _locador = locador.Locador(registro_nacional, nome, responsavel, telefone, email)
        _locador.cadastrar_locador()
    elif opcao == "3":
        # Imovel
        cod_imovel = input("Digite o codigo do imovel: ")
        valor = float(input("Digite o valor do imovel: "))
        tamanho = input("Digite o tamanho do imovel (em m²): ")
        numero_imovel = input("Digite o numero do imovel: ")
        andar = input("Digite o andar do imovel: ")
        _imovel = imovel.Imovel(cod_imovel, valor, tamanho, numero_imovel, andar)
        _imovel.cadastrar_imovel()
    else:
        print("opção invalida")
