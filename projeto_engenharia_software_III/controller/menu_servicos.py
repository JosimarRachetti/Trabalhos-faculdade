from model import manutencao_elevador, limpeza, funcionario
import uuid

def menu(opcao):
    if opcao == "1":
        #servico manuntencao
        cod_servico = input("Digite o codigo do servico: ")
        data_servico = input("Digite a data do servico: ")
        mecanico = input("Digite o nome do mecanico: ")
        cod_contrato = input("Digite o codigo do contrato: ")
        _manutencao = manutencao_elevador.ManutencaoElevador(cod_servico, data_servico, cod_contrato, mecanico)
        _manutencao.registrar_manutencao()
    elif opcao == "2":
        #servico limpeza
        cod_servico = input("Digite o codigo do servico: ")
        data_servico = input("Digite a data do serviço: ")
        andar = input("Digite o andar de limpeza: ")
        cod_funcionario = input("Digite o codigo do funcionario: ")
        cod_predio = input("Digite o codigo do predio: ")
        _limpeza = limpeza.Limpeza(cod_servico, data_servico, andar, cod_funcionario, cod_predio)
        _limpeza.registrar_limpeza()
    elif opcao == "3":
        #registrar funcionario
        cod_funcionario = input("Digite o codigo do funcionario: ")
        nome = input("Digite o nome do funcionario: ")
        cargo = input("Digite o cargo: ")
        empresa = input("Digite a empresa: ")
        _funcionario = funcionario.Funcionario(cod_funcionario, nome, cargo, empresa)
        _funcionario.registro_funcionario()
    else:
        print("Opcao inválida")


