import const


class Funcionario:
    def __init__(self, cod_funcionario, nome, cargo, empresa):
        self.cod_funcionario = cod_funcionario
        self.nome = nome
        self.cargo = cargo
        self.empresa = empresa

    def registro_funcionario(self):
        key = self.cod_funcionario
        info = [self.nome, self.cargo, self.empresa]
        DADOS = {key: info}
        const.db_lista_funcionario.update(DADOS)
