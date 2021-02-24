from conta import *
from pessoa import *
from pickle import dump, load


def abrir_conta(cliente):
    while True:
        print('1- Conta Corrente\n'
              '2- Conta Poupanca\n'
              '0- Sair')
        tipo_conta = input('Escolha seu tipo de conta: ')
        if tipo_conta == '1':
            print('Com a conta Corrente retirar R$500 mesmo sem saldo na conta')
            cliente.tipo_conta = ContaCorrente()
        elif tipo_conta == '2':
            print('Com a conta Poupanca voce ganha [10%] do valor depositado')
            cliente.tipo_conta = ContaPoupanca()
        elif tipo_conta == '0':
            print('Saindo...')
            exit(0)
        else:
            print('Comando invalido')
            continue
        cliente.nome = input('Digite seu nome: ')
        cliente.salvar_conta()
        break


def salvar_conta_db(contas):
    try:
        with open('database', 'wb') as arquivo:
            dump(contas, arquivo)
    except:
        print('Erro ao salvar')


def carregar_conta():
    try:
        with open('database', 'rb') as arquivo:
            conta_salva = load(arquivo)
            return conta_salva
    except:
        pass


if __name__ == '__main__':
    print('--------------------------------')
    print('\tBanco JSILVA N.Y')
    print('--------------------------------')
    print()
    print('Bem vindo ao JSILVA N.Y')
    conta_usuario = carregar_conta()
    if not conta_usuario:
        print('No banco existe dois tipos de contas: Corrente e Poupanca')
        while True:
            print(
                'Parece que Voce ainda nao tem uma Conta, deseja fazer? [s/n]')
            fazer_conta = input('Escolha: ')
            if fazer_conta == 's':
                conta_usuario = Pessoa()
                print('Escolha seu tipo de Conta: ')
                abrir_conta(conta_usuario)
                conta_usuario.informacoes_conta()
                salvar_conta_db(conta_usuario)
                break
            elif fazer_conta == 'n':
                print('Que pena, se mudar de ideia estou sempre aqui!')
                exit(0)
            else:
                print('Comando invalido')
    while True:
        print('\t-----MENU-----')
        print('1- Depositar\n'
              '2- Sacar\n'
              '3- Mostrar Saldo\n'
              '4- Informacoes da conta\n'
              '0- Sair')
        escolha = input('Escolha: ')
        if escolha == '1':
            deposito_valor = input('Digite o valor: ')
            conta_usuario.tipo_conta.depositar(deposito_valor)
            salvar_conta_db(conta_usuario)
        elif escolha == '2':
            sacar_valor = input('Digite o valor: ')
            conta_usuario.tipo_conta.sacar(sacar_valor)
            salvar_conta_db(conta_usuario)
        elif escolha == '3':
            conta_usuario.tipo_conta.mostrar_saldo()
        elif escolha == '4':
            conta_usuario.informacoes_conta()
        elif escolha == '0':
            print('Saindo...')
            exit(0)
