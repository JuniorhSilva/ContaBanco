from conta import *



class Pessoa():
    base_dados = {}

    def __init__(self, nome=None, tipo_conta=None):
        self.nome = nome
        self.tipo_conta = tipo_conta

    def __str__(self):
        return f'{self.nome}'

    def salvar_conta(self):
        self.base_dados[self.tipo_conta.numero_conta] = {'nome': self.nome,
                                                         'tipo_conta': self.tipo_conta.tipo_conta,
                                                         'saldo': self.tipo_conta.saldo}

    def informacoes_conta(self):
        print(f'Nome: {self}')
        print(f'Tipo da conta: {self.tipo_conta}')
        print(f'Numero da conta: {self.tipo_conta.numero_conta}')
        print(f'Saldo R$ {self.tipo_conta.saldo:.2f}'.replace('.', ','))
