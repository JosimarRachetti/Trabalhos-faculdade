import const

class FuncionarioOrganizacao:
    def __init__(self, cod_funcionario, nome, cargo, cod_organizacao):
        self.cod_funcionario = cod_funcionario
        self.nome = nome
        self.cargo = cargo
        self.cod_organizacao = cod_organizacao

    def registro_funcionario_organizacao(self):
        key = self.cod_funcionario
        info = [self.nome, self.cargo, self.cod_organizacao]
        DADOS = {key: info}
        const.db_lista_funcionario_organizacao.update(DADOS)