class Cliente:

    def __init__(self, nome, num_conta,saldo):
        self.nome = nome
        self.num_conta = num_conta
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

    def transferencia(self, num_conta1, num_conta2, valor):
        num_conta1.saldo=self.saldo - valor
        num_conta2.saldo=self.saldo + valor
        return num_conta1.saldo, num_conta2.saldo

class Banco:

    def adicionar_conta(self, nome, cpf, idade, num_conta):
        conta = nome, cpf, idade, num_conta
        self.contas.append(conta)

    def excluir(self, num_conta):
        self.contas.pop(num_conta)
        print("Conta excluida com sucesso!")