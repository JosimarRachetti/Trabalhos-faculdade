import const


class Lixeira:
    def __init__(self, cod_lixeira, capacidade, dia_recolhimento):
        # lixeira
        self.cod_lixeira = cod_lixeira
        self.capacidade = capacidade
        self.dia_recolhimento = dia_recolhimento

    def registrar_lixeira(self):
        key = self.cod_lixeira
        info = [self.capacidade, self.dia_recolhimento]
        DADOS = {key: info}
        const.db_lista_lixeira.update(DADOS)

