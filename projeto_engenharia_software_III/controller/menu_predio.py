from model import predio, lixeira, brigada_incendio, estacionamento, uso_vaga_estacionamento, funcionario_organizacao
import uuid


def menu(opcao):

    if opcao == "1":
        #Predio
        cod_predio =  input("Digite o codigo do predio: ")
        endereco = input("Digite o endereço do predio: ")
        numero = input("Digite o numero do predio: ")
        cep = input("Digite o numero do cpf: ")
        qtd_salas = input("Digite a quantidade de salas: ")
        cadastro_brigada(cod_predio)
        _predio = predio.Predio(cod_predio, endereco, numero, cep, qtd_salas)
        _predio.registrar_predio()
    elif opcao == "2":
        #UsoVagaEstacionamento
        cadastra_funcionari_org()
        cadastro_uso_vaga()
    else:
        print("opção inválida")


def cadastrar_estacionamento(cod_predio):
    print("digite abaixo as informações sobre o estacionamento\n")

    cod_estacionamento = str(uuid.uuid4())
    qtd_vagas = input("Digite a quantidade de vagas: ")

    _estacionamento = estacionamento.Estacionamento(cod_estacionamento, cod_predio, qtd_vagas)
    _estacionamento.registrar_estacionamento()


def cadastro_brigada(cod_predio):

    print("digite abaixo as informações sobre a brigada de incendio\n")
    chefe_brigada = input("Digite o chefe da brigada: ")
    qtd_extintores = input("Digite a quantidade de extintores: ")
    validade_extintores = input("Digite a validade extintores: ")
    qtd_luzes_emerg = input("Digite a quantidade luzes emergencias: ")
    data_ultim_treinado = input("Data ultimo treinamento: ")
    cod_contrato = input("Digite o codigo de contrato: ")

    _brigada_incendio = brigada_incendio.BrigadaIncendio(chefe_brigada,qtd_extintores,validade_extintores, qtd_luzes_emerg, data_ultim_treinado, cod_contrato, cod_predio)
    _brigada_incendio.registrar_brigada()


def cadastro_lixeira():
    print("digite abaixo as informações sobre a lixeira")

    cod_lixeira = str(uuid.uuid4())
    capacidade = input("Digite a capacidade da lixeira: ")
    dia_recolhimento = input("Digite o dia de recolhimentos: ")
    _lixeira = lixeira.Lixeira(cod_lixeira, capacidade, dia_recolhimento)
    _lixeira.registrar_lixeira()

def cadastro_uso_vaga():
    print("Digite as informações da vaga")
    cod_vaga = input("Digite o codigo da vaga: ")
    inicio_uso = input("Digite o inicio do uso: ")
    termino_uso = input("Digite o termino do uso: ")
    cod_funcionario_org =  input("Digite o codigo do funcionario de organizacao: ")
    cod_estacionamento = input("Digite o codigo estacionamento: ")
    _uso_vaga = uso_vaga_estacionamento.UsoVagaEstacionamento(cod_vaga, inicio_uso, termino_uso, cod_funcionario_org, cod_estacionamento)
    _uso_vaga.registro_uso_vaga_estacionamento()
def cadastra_funcionari_org():
    print("Digite as informações do funcionario que usará a vaga")
    cod_funcio_org = input("Digite o codigo do funcionario: ")
    nome = input("Digite o nome do funcionario: ")
    cargo = input("Digite o cargo do funcionario: ")
    cod_organizacao = input("Digite o codigo do organizacao: ")
    _funcionario_organizacao = funcionario_organizacao.FuncionarioOrganizacao(cod_funcio_org, nome, cargo, cod_organizacao)
    _funcionario_organizacao.registro_funcionario_organizacao()

