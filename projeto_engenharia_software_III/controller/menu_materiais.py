from model import pedido_material, material


def menu(opcao):
    if opcao == "1":
        cod_material = input("Digite o codigo do material: ")
        nome = input("Digite o nome do material: ")
        tipo = input("Digite o tipo de material: ")
        quantidade = input("Digite a quantidade: ")
        valor = input("Digite o valor: ")
        _material = material.Material(cod_material, nome, tipo, quantidade, valor)
        _material.registrar_material()
    elif opcao == "2":
        cod_pedido = input("Digite o codigo de pedido: ")
        data = input("Digite a data de pedido: ")
        cod_material = input("Digite o codigo do material: ")
        quantidade = input("Digite a quantidade: ")
        _pedido_material = pedido_material.PedidoMaterial(cod_pedido, data, cod_material, quantidade)
        _pedido_material.registro_pedido_material()
    else:
        print("opção inválida")