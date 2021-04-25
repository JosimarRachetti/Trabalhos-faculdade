import const


class ArmazenagemContrato:
    def __init__(self, cod_arquivo, tipo, data_contrato, validade, data_armazenamento, status):
        self.cod_arquivo = cod_arquivo
        self.tipo = tipo
        self.data_contrato = data_contrato
        self.validade = validade
        self.data_armazenamento = data_armazenamento
        self.status = status

    def cadastrar_armazenagem_contrato(self):
        key = self.cod_arquivo
        info = [self.tipo, self.data_contrato, self.validade, self.data_armazenamento, self.status]
        DADOS = {key: info}
        # envio para bd
        const.db_lista_locatario.update(DADOS)
