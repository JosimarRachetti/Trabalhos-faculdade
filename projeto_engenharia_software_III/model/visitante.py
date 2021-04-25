import const


class Visitante:
    def __init__(self, cod_visitante, nome, idade, documento):
        self.cod_visitante = cod_visitante
        self.nome = nome
        self.idade = idade
        self.documento = documento

    def registro_visitante(self):
        key = self.cod_visitante
        info = [self.nome, self.idade, self.documento]
        DADOS = {key: info}
        const.db_visitante.update(DADOS)
