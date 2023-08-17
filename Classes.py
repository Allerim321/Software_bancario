class Cliente:

    def __init__(self, nome, cpf, idade, saldo):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            print("Não é possível sacar esse valor")
        else:
            self.saldo -= valor
            print("Valor sacado com sucesso! Seu saldo agora é de R$", self.saldo)

    def depositar(self, valor):
        self.saldo += valor
        print("Valor depositado com sucesso! Seu saldo agora é de R$", self.saldo)


class Conta:

    def __init__(self, saldo, cliente):
        self.saldo = saldo
        self.cliente = cliente


class Banco:

    def __init__(self):
        self.contas = []

    def adicionar_conta(self, saldo, cliente):
        conta = Conta(saldo, cliente)
        self.contas.append(conta)
