from uuid import uuid4
from model import armazenagem_contrato,contrato_imovel,contrato_serviço, contas, cotas_condominio


def menu(opcao):

    if opcao == "1":
        #contrato imovel
        cod_contrato = input("Digite o codigo de contrato: ")
        valor = input("Digite o valor do contrato: ")
        validade = input("Digite a validade do contrato: ")
        data = input("Digite a validade do contrato: ")
        _contrato_imovel = contrato_imovel.ContratoImovel(cod_contrato, valor, valor, data)
        _contrato_imovel.cadastrar_imovel()
    elif opcao == "2":
        #contrato servico
        cod_contrato = input("Digite o codigo do contrato: ")
        area_servico = input("Digite a area de serviço do contrato: ")
        tipo_servico = input("Digite o tipo de serviço: ")
        valor = input("Digite o valor do contrato: ")
        validade = input("Digite a validade do contrato: ")
        data = input("Digite a validade do contrato: ")
        _contrato_servico = contrato_serviço.ContratoServico(cod_contrato, area_servico, data, valor, tipo_servico, validade)
        _contrato_servico.cadastrar_armazenagem_contrato()
    elif opcao == "3":
        #contas
        cod_contas = input("Digite o codigo da conta: ")
        tipo = input("Digite o tipo da conta: ")
        data_emissao = input("Digite a data de emissão: ")
        valor = input("Digite o valor: ")
        data_vencimento = input("Digite a data de vencimento: ")
        data_pagamento = input("Digite a data de pagamento: ")
        multa = input("Digite a multa(se houver): ")
        _contas = contas.Contas(cod_contas, tipo, data_emissao, valor, data_vencimento, data_pagamento, multa)
        _contas.registrar_contas()
    elif opcao == "4":
        #armazenamento_contrato
        cod_arquivo = input("Digite o codigo do arquivo: ")
        tipo = input("Digite o tipo de arquivo: ")
        data_contrato = input("Digite a data do contrato: ")
        validade = input("Digite a validade do contrato: ")
        data_armazenamento = input("Digite a data armazenamento: ")
        _armazenagem_contrato = armazenagem_contrato.ArmazenagemContrato(cod_arquivo, tipo, data_contrato, validade, data_armazenamento)
        _armazenagem_contrato.cadastrar_armazenagem_contrato()
    elif opcao == "5":
        cod_cota = input("Digite o codigo da cota: ")
        data_emissao = input("Digite a data da emissao: ")
        valor = input("Digite o valor da cota: ")
        data_vencimento = input("Digite a data do vencimento: ")
        data_pagamento = input("Digite data pagamento: ")
        multa = input("Digite valor multa (se houver): ")
        _contas_condominio = cotas_condominio.CotasCondominio(cod_cota, data_emissao, valor, data_vencimento, data_pagamento, multa)
        _contas_condominio.registro_cotas()
    else:
        print("opção inválida")