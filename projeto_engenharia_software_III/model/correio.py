import const


class Correio:
    def __init__(self, cod_recebimento, remetente, destinatario, data_recebimento, data_entrega):
        self.cod_recebimento = cod_recebimento
        self.remetente = remetente
        self.destinatario = destinatario
        self.data_recebimento = data_recebimento
        self.data_entrega = data_entrega

    def registro_entrega(self):
        key = self.cod_recebimento
        info = [self.remetente, self.destinatario, self.data_recebimento, self.data_entrega]
        DADOS = {key: info}
        const.db_lista_correio.uptade(DADOS)
