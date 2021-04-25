import const


class BrigadaIncendio:
    def __init__(self, chefe_brigada, qtd_extintores, validade_extintores, qtd_luzes_emerg, data_ultim_treinamento, cod_contrato, cod_predio):
        self.chefe_brigada = chefe_brigada
        self.qtd_extintores = qtd_extintores
        self.validade_extintores = validade_extintores
        self.qtd_luzes_emerg = qtd_luzes_emerg
        self.data_ultim_treinamento = data_ultim_treinamento
        self.cod_contrato = cod_contrato
        self.cod_predio = cod_predio

    def registrar_brigada(self):
        key = self.cod_contrato
        info = [self.chefe_brigada, self.qtd_extintores, self.validade_extintores, self.qtd_luzes_emerg, self.data_ultim_treinamento, self.cod_contrato]
        DADOS = {key: info}
        const.db_lista_brigada.update(DADOS)


