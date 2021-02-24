from random import randint
from time import sleep
from random import random


class Conta:
    def __init__(self, numero_conta=None, saldo=0, digito='-0', tipo_conta=None):
        if numero_conta is None:
            numero_conta = str(randint(1000000, 9999999)) + digito
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.tipo_conta = tipo_conta

    def __str__(self):
        return f"{self.tipo_conta}"

    def mostrar_saldo(self):
        print(
            f"Seu saldo: R$ {float(self.saldo):.2f}".replace('.', ','))

    def sacar(self, total_sacar):
        while True:
            try:
                total_sacar = float(total_sacar)
                if total_sacar > 0:
                    if self.saldo >= total_sacar:
                        self.saldo -= total_sacar
                        print('Transação concluida com sucesso!')
                        self.mostrar_saldo()
                        return self.saldo
                    else:
                        print('Saldo insuficiente')
                        break
                else:
                    print('Valor inserido é invalido')
                    break
            except ValueError:
                print('Valor invalido')
                break

    def depositar(self, valor):
        try:
            valor = float(valor)
            if valor > 0:
                self.saldo += valor
                print('Deposito feito com sucesso')
                self.mostrar_saldo()
            else:
                print('So pode depositar valor acima de R$ 0,00')
        except ValueError:
            print('Valor invalido')
        except TypeError:
            print('Valor invalido')

    def investir(self, valor):
        try:
            valor = float(valor)
            if self.saldo > 0:
                if valor > 0:
                    print('Investindo...')
                    sleep(5.0)
                    possibilidade = random()
                    if possibilidade >= 0.8:
                        aumento = valor * 0.5
                        self.saldo += aumento
                        print(
                            f'Voce deu sorte ganhou um total de R${aumento:.2f}'.replace('.', ','))
                    elif possibilidade <= 0.4:
                        aumento = valor * 0.15
                        self.saldo += aumento
                        print(f'Ganhou R${aumento:.2f}'.replace('.', ','))
                    else:
                        aumento = valor * 0.10
                        print(
                            f'Que pena voce perdeu: R${aumento:.2f}'.replace('.', ','))
                        self.saldo -= aumento
                    self.mostrar_saldo()
                else:
                    print('Valor invalido')
            else:
                print('Conta negativa')
        except ValueError:
            print('Valor invalido')
        except TypeError:
            print('Valor invalido')


class ContaPoupanca(Conta):
    def __init__(self, numero_conta=None, saldo=0, digito='-0', tipo_conta=None):
        tipo_conta = 'Poupanca'
        super().__init__(numero_conta, saldo, digito, tipo_conta)

    def depositar(self, valor):
        while True:
            try:
                valor = float(valor)
                aumento10 = valor + (valor * 0.10)
                self.saldo += aumento10
                print('Deposito feito com sucesso')
                self.mostrar_saldo()
                break
            except ValueError:
                print('Valor invalido')
                break
            except TypeError:
                print('Valor invalido')
                break


class ContaCorrente(Conta):
    def __init__(self, numero_conta=None, saldo=0, limite=500, digito='-1', tipo_conta=None):
        self.limite = limite
        tipo_conta = 'Corrente'
        super().__init__(numero_conta, saldo, digito, tipo_conta)

    def sacar(self, total_sacar):
        while True:
            try:
                total_sacar = float(total_sacar)
                limite_conta = self.saldo + self.limite
                if total_sacar > 0:
                    if limite_conta >= total_sacar:
                        self.saldo -= total_sacar
                        print('Transação concluida com sucesso!')
                        print(
                            f'Saldo Retirado: R${total_sacar:.2f}'.replace('.', ','))
                        self.mostrar_saldo()
                        return self.saldo
                    else:
                        print('Sem limite na conta')
                        break
                else:
                    print('Valor digitado é invalido')
                    break
            except ValueError:
                print('Valor invalido')
                break
            except TypeError:
                print('Valor invalido')
                break
