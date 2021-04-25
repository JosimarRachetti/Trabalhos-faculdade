import const


class Limpeza:
    def __init__(self, cod_limpeza, data, andar, funcionario, cod_predio):
        self.cod_limpeza = cod_limpeza
        self.data = data
        self.andar = andar
        self.funcionario = funcionario
        self.cod_predio = cod_predio

    def registrar_limpeza(self):
        key = self.cod_limpeza
        info = [self.data, self.andar, self.funcionario, self.cod_predio]
        DADOS = {key: info}
        const.db_lista_limpeza.update(DADOS)


