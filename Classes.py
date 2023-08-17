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

    def transferencia(self, cpf1, cpf2, valor):
        self.cpf1=input("Defina o cpf de quem irá transferir.\n-")
        self.cpf2=input("Defina o cpf de quem irá receber.\n-")
        self.valor=input("Defina o valor a ser transferido.\n-")
        cpf1.saldo=self.saldo - valor
        cpf2.saldo=self.saldo + valor
        return cpf1.saldo, cpf2.saldo

class Banco:

    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj

    def __init__(self):
        self.contas = []

    def adicionar_conta(self, nome, cpf):
        conta = Cliente(nome, cpf)
        self.contas.append(conta)

    def excluir(self, cpf):
        self.contas.pop(cpf)
        print("Conta excluida com sucesso!")