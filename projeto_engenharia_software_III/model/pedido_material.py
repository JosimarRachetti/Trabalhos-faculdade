import const


class PedidoMaterial:
    def __init__(self, cod_pedido, date, cod_material, qtd):
        self.cod_pedido = cod_pedido
        self.date = date
        self.cod_material = cod_material
        self.qtd = qtd

    def registro_pedido_material(self):
        key = self.cod_pedido
        info = [self.date, self.cod_material, self.qtd]
        DADOS = {key: info}
        const.db_lista_pedido_material.update(DADOS)