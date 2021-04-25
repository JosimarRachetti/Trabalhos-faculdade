import const

class Predio:
    def __init__(self, cod_predio, endereco, numero, cep, qtd_salas):
        self.cod_predio = cod_predio
        self.endereco = endereco
        self.numero = numero
        self.cep = cep
        self.qtd_salas = qtd_salas

    def registrar_predio(self):
        key = self.cod_predio
        info = [self.endereco, self.numero, self.cep, self.qtd_salas]
        DADOS = {key: info}
        const.db_lista_predios.update(DADOS)