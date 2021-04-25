import const

class Locatario:
    def __init__(self, cnpj, razao_social, responsavel, telefone, email):
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.responsavel = responsavel
        self.telefone = telefone
        self.email = email

    def cadastrar_locatario(self):
        key = self.cnpj
        info = [self.razao_social, self.responsavel, self.telefone, self.email]
        DADOS = {key: info}
        #envio para bd
        const.lista_locatario.update(DADOS)



