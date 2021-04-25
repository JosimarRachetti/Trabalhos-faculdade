import const


class Estacionamento:
    def __init__(self, cod_estacionamento, cod_predio, qtd_vagas):
        self.cod_estacionamento = cod_estacionamento
        self.cod_predio = cod_predio
        self.qtd_vagas = qtd_vagas

    def registrar_estacionamento(self):
        key = self.cod_estacionamento
        info = [self.cod_predio, self.qtd_vagas]
        DADOS = {key: info}
        const.db_lista_estacionamento.update(DADOS)