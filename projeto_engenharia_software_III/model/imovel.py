import const


class Imovel:
    def __init__(self, cod_imovel, valor, tamanho, numero_imovel, andar):
        self.cod_imovel = cod_imovel
        self.valor = valor
        self.tamanho = tamanho
        self.numero_imovel = numero_imovel
        self.andar = andar

    def cadastrar_imovel(self):
        key = self.cod_imovel
        info = [self.valor, self.tamanho, self.numero_imovel, self.andar]
        DADOS = {key: info}
        # envio para bd
        const.db_lista_locatario.update(DADOS)
