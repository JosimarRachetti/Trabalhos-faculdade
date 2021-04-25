import const

class CotasCondominio:
    def __init__(self, cod_cota, data_emissao, valor, data_venci, data_pagamento, multa):
        self.cod_cota = cod_cota
        self.data_emissao = data_emissao
        self.valor = valor
        self.data_venci = data_venci
        self.data_pagamento = data_pagamento
        self.multa = multa

    def registro_cotas(self):
        key = self.cod_cota
        info = [self.data_emissao, self.valor, self.data_venci, self.data_pagamento, self.multa]
        DADOS = {key: info}
        const.db_lista_cotas.update(DADOS)
