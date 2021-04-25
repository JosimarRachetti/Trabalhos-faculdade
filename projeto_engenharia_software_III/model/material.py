import const

class Material:
    def __init__(self, cod_material, nome, tipo, quantidade, valor):
        self.cod_material = cod_material
        self.nome = nome
        self.tipo = tipo
        self.quantidade = quantidade
        self.valor = valor

    def registrar_material(self):
        key = self.cod_material
        info = [self.nome, self.tipo, self.quantidade, self.valor]
        DADOS = {key: info}
        const.db_lista_material.update(DADOS)
