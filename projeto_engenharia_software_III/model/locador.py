import const


class Locador:
    def __init__(self, registro_nacional, nome, responsavel, telefone, email):
        self.registro_nacional = registro_nacional
        self.nome = nome
        self.responsavel = responsavel
        self.telefone = telefone
        self.email = email

    def cadastrar_locador(self):
        key = self.registro_nacional
        info = [self.nome, self.responsavel, self.telefone, self.email]
        DADOS = {key: info}
        # envio para bd
        const.lista_locatario.update(DADOS)
