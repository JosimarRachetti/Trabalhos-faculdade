import const


class UsoVagaEstacionamento:
    def __init__(self, cod_vaga, inicio_uso, termino_uso, cod_funcionario, cod_estacionamento):
        self.cod_vaga = cod_vaga
        self.inicio_uso = inicio_uso
        self.termino_uso = termino_uso
        self.cod_funcionario = cod_funcionario
        self.cod_estacionamento = cod_estacionamento

    def registro_uso_vaga_estacionamento(self):
        key = self.cod_vaga
        info = [self.inicio_uso, self.termino_uso, self.cod_funcionario, self.cod_estacionamento]
        DADOS = {key: info}
        const.db_lista_uso_vaga.update(DADOS)
