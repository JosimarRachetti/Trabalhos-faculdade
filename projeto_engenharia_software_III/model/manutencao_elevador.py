import const


class ManutencaoElevador:
    def __init__(self, cod_servico, data_servico, cod_contrato, mecanico):
        self.cod_servico = cod_servico
        self.data_servico = data_servico
        self.cod_contrato = cod_contrato
        self.mecanico = mecanico

    def registrar_manutencao(self):
        key = self.cod_contrato
        info = [self.data_servico, self.cod_contrato, self.mecanico]
