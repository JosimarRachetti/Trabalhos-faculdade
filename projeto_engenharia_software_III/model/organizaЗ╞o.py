import const


class Organizacao:
    def __init__(self, cod_organizacao, nome, cnpj, andar, telefone):
        self.cod_organizacao = cod_organizacao
        self.nome = nome
        self.cnpj = cnpj
        self.andar = andar
        self.telefone = telefone

    def registrar_organizacao(self):
        key = self.cod_organizacao
        info = [self.nome, self.cnpj, self.andar, self.telefone]
        DADOS = {key: info}
        const.db_organizacao.update(DADOS)
