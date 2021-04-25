import const

class Contas:
    def __init__(self, cod_conta, tipo, data_emissao, valor, data_vencimento, data_pagamento, multa):
        self.cod_conta = cod_conta
        self.tipo = tipo
        self.data_emissao = data_emissao
        self.valor = valor
        self.data_vencimento = data_vencimento
        self.data_pagamento = data_pagamento
        self.multa = multa

    def registrar_contas(self):
        key = self.cod_conta
        info = [self.tipo, self.data_emissao, self.valor, self.data_vencimento, self.data_pagamento, self.multa]
        DADOS = {key: info}
        const.db_lista_conta.update(DADOS)
