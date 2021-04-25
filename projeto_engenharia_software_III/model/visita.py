import const

class Visita:
    def __init__(self, cod_visita, horario, cod_organizacao, cod_visitante):
        self.cod_visita = cod_visita
        self.horario = horario
        self.cod_organizacao = cod_organizacao
        self.cod_visitante = cod_visitante

    def registro_visita(self):
        key = self.cod_visita
        info = [self.horario, self.cod_visitante, self.cod_organizacao]
        DADOS = {key: info}
        const.db_visita.update(DADOS)
