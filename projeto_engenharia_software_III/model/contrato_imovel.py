import const


class ContratoImovel:
    def __init__(self, cod_contrato, valor, validade, data):
        self.cod_contrato = cod_contrato
        self.valor = valor
        self.validade = validade
        self.data = data

    def cadastrar_imovel(self):
        key = self.cod_contrato
        info = [self.valor, self.data, self.valor, self.validade]
        DADOS = {key: info}
        # envio para bd
        const.db_lista_imovel.update(DADOS)
