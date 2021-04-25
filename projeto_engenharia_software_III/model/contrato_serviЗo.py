import const


class ContratoServico:
    def __init__(self, cod_contrato, area_servico, data, valor, tipo_servico, validade):
        self.cod_contrato = cod_contrato
        self.area_servico = area_servico
        self.data = data
        self.valor = valor
        self.tipo_servico = tipo_servico
        self.validade = validade

    def cadastrar_armazenagem_contrato(self):
        key = self.cod_contrato
        info = [self.area_servico, self.data, self.valor, self.tipo_servico, self.validade]
        DADOS = {key: info}
        # envio para bd
        const.db_lista_locatario.update(DADOS)
